program test3
    implicit none
    dimension f(10),g(10)
    real f,g
    integer i,j

    do i = 1, 10
        if(i == 1)then
            f(i) = 0
        else if(i == 2)then
            f(i) = 1
        else
            f(i) = f(i-1) + f(i-2)
        end if
    end do

    write(*,*) f
    do j = 1, 10
        g(j) = f(j)
    end do

    write(*,*) g
end program test3