program test1
    implicit none
    real x0,x1
    integer n
    character t

    n = 1;x1 = 2
    x0 = 1
    t = '2'! 1, 2, 3
    call iterative(x0,x1,n,t)

end program test1

recursive subroutine iterative(x1,x2,n,t)
    implicit none
    real f, y1, y2, x1, x2
    integer n
    character t
    
    if (abs(x2-x1) > 1E-3)then
        y1 = f(x1,t)
        y2 = f(y1,t)
        x2 = (x1*y2 - y1**2)/(x1 - 2*y1 + y2)
        write(*,*) n, x2 ,abs(x2-x1)
        n = n+1
        call iterative(x2,x1,n,t)
    end if

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
