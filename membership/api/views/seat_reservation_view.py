from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.db.transaction import atomic
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils import timezone

from screens.api.pagination import StandardResultsPagination
from screens.models import Screen, Row, Seat
from membership.models import User


class SeatReservationCreateAPIView(APIView):
    # permission_classes = (IsAuthenticated,)
    pagination_class = StandardResultsPagination

    @atomic
    def post(self, request, *args, **kwargs):
        """
        Allows user to reserve tickets based upon selection by the user
        - Checks if the requested rows exists in the screen
        - Checks if the requested seats exists in the row and are not already reserved
        - If all the conditions are satisfied, reserves tickets
        """
        user = User.objects.get(id=1)
        screen_name = kwargs.get('screen_name', None)
        
        screen = get_object_or_404(Screen, screen_name=screen_name)

        seats = request.data.get('seats', None)

        if seats is None:
            return Response("Please check requested seats.", 
                            status=status.HTTP_400_BAD_REQUEST)

        rows = seats.keys()
        total_screen_rows = screen.rows.filter(row_char__in=rows).count()

        # Check if requested seat rows exists in the screen.
        if not(len(rows) == total_screen_rows):
            return Response("Requested row does not exists", 
                            status=status.HTTP_400_BAD_REQUEST)

        for row_char in rows:
            row = screen.rows.get(row_char=row_char)
            seat_nos = seats.get(row_char, None)
            to_reserve_seats = (row
                                .seats
                                .filter(seat_no__in=seat_nos, 
                                        is_reserved=False)
                                .count()
                                )

            # requested seats are not reserved already
            if not(to_reserve_seats == len(seat_nos)):
                return Response("Request seats are either reserved or do not exists.", 
                            status=status.HTTP_403_Forbidden)

        for row_char in rows:
            seat_nos = seats.get(row_char, None)
            (Seat
            .objects
            .filter(seat_no__in=seat_nos,
                    row__row_char=row_char,
                    is_reserved=False)
            .update(is_reserved=True,
                    reserved_by=user,
                    reserved_at=timezone.now())
            )

        return Response("Your seats have been successfully reserved", 
                        status=status.HTTP_200_OK)
