program test2
    implicit none
    real f, x0, x1, a
    integer n
    character t

    n = 1; a = 1; x1 = 2
    x0 = 0
    t = '3'! 1, 2, 3
    do while((abs(x1-a) > 1E-5))
        if (n == 1)then
            a = x0
        else
            a = x1
        end if

        x1 = f(a,t)
        write(*,*) n, x1, abs(x1-a)

        n = n+1
    end do
end program test2

real function f(x,type)
    implicit none
    character type
    real x
    if (type == '1')then
        f = (cos(x)+sin(x))/4
    else if (type == '2')then
        f = log(4-x)/log(2.0) 
    else if (type == '3')then
        if (x < 0)then
            f = -(abs(3*x+1)/2)**(1.0/3.0)
        else
            f = ((3*x+1)/2)**(1.0/3.0)
        end if
    end if
end function f