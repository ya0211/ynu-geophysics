program test1
    implicit none
    real x0
    integer n

    n = 1
    x0 = 0
    call iterative(x0,n)

end program test1

recursive subroutine iterative(x1,n)
    implicit none
    real, intent(in)::x1
    real x2
    integer n

    x2 = x1 - (exp(x1)-4*x1)/(exp(x1)-4)
    write(*,*) n, x2
    n = n+1
    if (abs(x2-x1) < 1E-5)then
        stop
    end if
    call iterative(x2,n)

    return

end subroutine iterative

