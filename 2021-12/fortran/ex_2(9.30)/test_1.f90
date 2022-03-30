program test1
    implicit none
    real a,b
    integer i
    a = 1
    b = 1

    do i = 2,10
        a = a*i
        !write(*,*) a
        b = b+1/(a)
    end do
    write(*,*) b
end program test1