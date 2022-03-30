subroutine judge(u, x, i)
    implicit none
    integer, intent(out)::i
    real u, x
    dimension x(100)

    do i = 1, 100
        if ( u < x(i) ) then
            return
        end if
    end do 

end subroutine judge

real function a(k, j, u, x)
    implicit none
    integer k, j, c
    real u, x
    dimension x(100)
    a = 1

    do c = j-1, j+1
        if ( k /= c ) then
            a = a * (u-x(c)) / (x(k)-x(c))
        end if
    end do
    return

end function a 

real function function_y(x)
    implicit none
    real x

    function_y = sin(x)
    return

end function function_y

subroutine main(u, i, y)
    implicit none
    real, intent(out)::y
    integer, intent(out)::i
    real u, array_x, pi
    real a, function_y
    dimension array_x(100)
    integer n, e
    pi = 3.1415926535898

    y = 0
    do n = 1, 100
        array_x(n) = y
        y = y + 2*pi/100
    end do

    call judge(u, array_x, i)
    if ( abs(u - array_x(i)) > abs(u - array_x(i-1)) ) then
        i = i-1
    end if

    y = 0
    do e = i-1, i+1
        y = y + a(e, i, u, array_x) * function_y(array_x(e))
    end do
    return

end subroutine main

program test1
    implicit none
    integer i
    real u, y

    u = 1.4
    call main(u, i, y)

    write(*,*) "u =", u
    write(*,*) "i =", i
    write(*,*) "y(u) =", y
    write(*,*) "sin(u) =", sin(u)
    write(*,*) "|yu-sin(u)|=", abs(y-sin(u))

end program test1
