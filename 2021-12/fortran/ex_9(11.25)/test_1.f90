program test1
    implicit none
    real x0,x1
    integer n,k

    n = 1
    x0 = 0; x1 = 1
    k = 1 ! 1, 2
    call iterative(x0,x1,n,k)

end program test1

recursive subroutine iterative(x1,x2,n,j)
    implicit none
    real f, x1, x2, x3
    integer n,j

    if (abs(x2-x1) > 1E-5)then
        x3 = x2 - (x2-x1)*f(x2,j)/(f(x2,j)-f(x1,j))
        write(*,*) n, x3 ,abs(x3-x2)
        n = n+1
        call iterative(x2,x3,n,j)
    end if

    return

end subroutine iterative

real function f(x,i)
    implicit none
    integer i
    real x

    if (i == 1)then
        f = 1-x-sin(x)
    else if (i == 2)then
        f = exp(2*x)+x-4
    end if
end function f