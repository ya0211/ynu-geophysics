program test1
    implicit none
    real a,b,e,x
    integer i

    a = 1.0
    b = 1.5
    i = 1

    do while(1 == 1)
        call dichotomy(a,b,x)
        e = abs(b-a)
        write(*,*) i, (a+b)/2
        if(e < 1E-3)then
            exit
        end if
        i = i+1
    end do
    
end program test1

subroutine dichotomy(a,b,x)
    implicit none
    real f,a,b,e,x
    if(f((a+b)/2) == 0)then
        x = (a+b)/2
        e = 0
    else
        if(f((a+b)/2)*f(a) < 0)then
            b = (a+b)/2
        else
            a = (a+b)/2
        end if
    end if
    return
end subroutine dichotomy

real function f(x)
    implicit none
    real x
    f = x**3-x-1
    return
end function f