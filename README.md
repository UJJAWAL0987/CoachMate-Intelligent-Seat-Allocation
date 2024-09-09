# CoachMate: Intelligent Seat Allocation

**CoachMate** is a smart seat allocation system designed for a train coach with 80 seats, organized into 7 seats per row, except for the last row, which has only 3 seats. This application allows users to reserve up to 7 seats at a time, ensuring that seats are prioritized by row and proximity.

## Features
- **80 Seat Capacity**: One coach with 80 seats, arranged in rows of 7, except for the last row with 3 seats.
- **Row-Priority Booking**: Seats are booked in the same row when available.
- **Proximity-Based Allocation**: If a row does not have enough seats, the system intelligently assigns the nearest available seats.
- **Flexible Reservation**: Users can book multiple seats (up to 7 at a time) until the coach is full.
- **Simple Interface**: No login functionality is required, allowing users to focus on reserving seats quickly and efficiently.

## Problem Description
1. The train coach has 80 seats, arranged into rows of 7, with the last row containing only 3 seats.
2. Users can reserve up to 7 seats in one booking.
3. Priority is given to reserving seats within the same row.
4. If a row does not have enough seats, nearby seats are reserved to keep groups together.
5. Users can continue booking until all seats are occupied.
6. No login functionality is required for this application.

## How It Works
1. **Seat Allocation Logic**:
   - When a user selects a number of seats to reserve, CoachMate first checks if enough seats are available in one row.
   - If the seats cannot be placed in a single row, CoachMate finds the closest available seats in the coach and assigns them.
   
2. **Edge Cases**:
   - If fewer than 7 seats are left, CoachMate automatically allocates whatever seats are available.
   - Once all 80 seats are reserved, further bookings are blocked.


