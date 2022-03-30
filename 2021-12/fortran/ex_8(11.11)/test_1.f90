program test1
    implicit none
    real x0,x1,pi
    integer n,t

    n = 1; x1 = 100; pi=3.1415926
    x0 = 1
    t = 3 ! 1, 2, 3
    call iterative(x0,x1,n,t)

end program test1

recursive subroutine iterative(x1,x2,n,t)
    implicit none
    real f, x1, x2
    integer n,t
    
    if (abs(x2-x1) > 1E-4)then
        x2 = x1 - f(x1,0,t)/f(x1,1,t)
        write(*,*) n, x2 ,abs(x2-x1)
        n = n+1
        call iterative(x2,x1,n,t)
    end if

    return

end subroutine iterative

real function f(x,d,t)
    implicit none
    integer t,d
    real x

    if (t == 1)then
        if (d == 0)then
            f = exp(2*x)+x-4
        else
            f = 2*exp(2*x)+1
        end if
    else if (t == 2)then
        if (d == 0)then
            f = sin(x)-x/2
        else
            f = cos(x)-0.5
        end if
    else if (t == 3)then
        if (d == 0)then
            f = x**3+2*x**2+10*x-20
        else
            f = 3*x**2+4*x+10
        end if
    end if
end function f