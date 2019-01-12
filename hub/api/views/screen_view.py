from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.db.transaction import atomic
from django.shortcuts import get_object_or_404
from django.urls import reverse

from screens.api.pagination import StandardResultsPagination
from screens.models import Screen, Row, Seat
from membership.models import User


class MovieScreenCreateListAPIView(APIView):
    # permission_classes = (IsAuthenticated,)
    pagination_class = StandardResultsPagination

    @atomic
    def post(self, request, *args, **kwargs):
        """
        endpoint: /screens
        method: post

        This view creates screen and stores information about seats and other related
        data.
        """
        user = User.objects.get(id=1)

        screen_name = request.data.get('name', None)

        if screen_name is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        screen = (Screen
                  .objects
                  .create(screen_name=screen_name, created_by=user)
                  )

        seat_data = request.data.get('seatInfo', None)

        if seat_data is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        rows_data = seat_data.keys()

        for row in rows_data:
            seat_model_create_list = []
            total_seats = seat_data.get(row).get('numberOfSeats', None)
            aisle_seats = seat_data.get(row).get('aisleSeats', None)            
            
            row = (Row
                   .objects
                   .create(row_char=row,
                           screen=screen,
                           total_seats=total_seats
                           )
                   )

            for index in range(total_seats): 
                seat_model_create_list.append(
                    Seat(seat_no=index,
                         row=row)
                )

            Seat.objects.bulk_create(seat_model_create_list)
            
            (Seat
            .objects
            .filter(seat_no__in=aisle_seats)
            .update(is_aisle_seat=True)
            )

        return Response(status=status.HTTP_201_CREATED)
