program test4
    implicit none
    real a,b,c
    real d,x1,x2

    write(*,*) 'Enter the coefficient "a,b,c" of the quadratic equation (ax^2+bx+c=0)'
    read(*,*)a,b,c

    d = b**2 -4*a*c
    x1 = (-b +sqrt(d))/(2*a)
    x2 = (-b -sqrt(d))/(2*a)
    if(d > 0)then
        write(*,*) 'x1 = ', x1, 'x2 = ', x2
    else if(d == 0)then
        write(*,*) 'x1 = x2 = ', x1
    else
        write(*,*) 'The equation has no real roots'
    end if

end program test4