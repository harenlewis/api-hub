import re

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


class ScreenSeatsListAPIView(APIView):
    # permission_classes = (IsAuthenticated,)
    pagination_class = StandardResultsPagination

    def get(self, request, format=None, *args, **kwargs):
        """
        This view handles two requests together based upon the query parameters
        """
        response_obj = {}
        user = User.objects.get(id=1)
        screen_name = kwargs.get('screen_name', None)

        screen = get_object_or_404(Screen, screen_name=screen_name)

        status = request.query_params.get('status', None)
        
        num_seats = request.query_params.get('numSeats', None)
        choice = request.query_params.get('choice', None)

        if status is not None:
            unreserved_seats = {"seats": {}}
            screen_rows = screen.rows.all()
            for row in screen_rows:
                row_char = row.row_char            
                unreserved_row_seats = (row
                                        .seats
                                        .filter(is_reserved=False)
                                        .values_list('seat_no', flat=True)
                                        )

                if row_char not in unreserved_seats.get('seats'):
                    unreserved_seats['seats'][row_char] = unreserved_row_seats
                else:
                    unreserved_seats['seats'][row_char] = unreserved_row_seats

            response_obj.update(unreserved_seats)

        if num_seats is not None and choice is not None:

            match = re.match(r"([a-z]+)([0-9]+)", choice, re.I)
            if match:
                items = match.groups()
                try:
                    row_char = items[0]
                    seat_no = items[1]
                except IndexError:
                    return Response(response_obj)
                # import pdb; pdb.set_trace()
                row = screen.rows.filter(row_char=row_char)

                if row.exists():
                    row = row[0]
                    available_seats = { "availableSeats": { row_char: [] } }
                    seat_list = self.find_continous_seats(row, seat_no, num_seats)
                    
                    if seat_list is not None:
                        available_seats['availableSeats'][row_char] = seat_list
                        response_obj.update(available_seats)
                    else:
                        return Response("Sorry no continous seats found", 
                                        status=status.HTTP_404_NOT_FOUND)

        return Response(response_obj)

    def find_continous_seats(self, row, seat_no, num_seats):
        """
        Checks seats to the left, right and of the requested seat no
        Also if the seat is the mid seat.
        """
        left_seats_list = []
        right_seats_list  = []
        middle_seat_list = []
        num_seats = int(num_seats)
        seat_no = int(seat_no)

        mid_range_left = seat_no - int(num_seats/2)

        mid_range_right = seat_no - int(num_seats/2) + 1

        if not (mid_range_left < 0 and mid_range_right > row.total_seats):
            for n in range(mid_range_left, mid_range_right+1):
                middle_seat_list.append(n)

        left_range = seat_no - num_seats -1

        if not (left_range < 0):
            for n in range(left_range, seat_no+1):
                left_seats_list.append(n)

        right_range = seat_no + num_seats -1

        if not (right_range > row.total_seats):
            for n in range(seat_no, right_range+1):
                right_seats_list.append(n)

        left_seats_available = (row
                                .seats
                                .filter(seat_no__in=left_seats_list, 
                                        is_reserved=False,
                                        is_aisle_seat=False)
                                .count()
                                )
        
        right_seats_available = (row
                                .seats
                                .filter(seat_no__in=right_seats_list, 
                                        is_reserved=False,
                                        is_aisle_seat=False)
                                .count()
                                )

        middle_seats_available = (row
                                .seats
                                .filter(seat_no__in=middle_seat_list, 
                                        is_reserved=False,
                                        is_aisle_seat=False)
                                .count()
                                )

        if left_seats_available == num_seats:
            return left_seats_list
        elif right_seats_available == num_seats:
            return right_seats_list
        elif middle_seats_available == num_seats:
            return middle_seat_list
        else:
            return None

