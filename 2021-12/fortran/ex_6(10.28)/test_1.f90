program test1
    implicit none
    real x0
    integer n
    character t

    n = 1
    x0 = 0.3
    t = '1'! 1, 2, 3
    call iterative(x0,n,t)

end program test1

recursive subroutine iterative(x1,n,t)
    implicit none
    real, intent(in)::x1
    real f, x2
    integer n
    character t

    x2 = f(x1,t)
    write(*,*) n, x2
    n = n+1
    if (abs(x2-x1) < 1E-5)then
        stop
    end if
    call iterative(x2,n,t)

    return

end subroutine iterative

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
