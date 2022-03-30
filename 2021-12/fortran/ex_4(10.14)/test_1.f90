program test1
    implicit none
    integer i
    real r,s

    open(1, file = 'radius.txt')
    open(2, file = 'area.txt')

    do i = 1, 10
        read(1,*) r
        !write(*,*) r
        call calculate(r,s)
        write(2,*) s
    end do

    close(1)
    close(2)

end program test1

subroutine calculate(r,s)
    implicit none
    real r,s
    s = 3.1415*r**2
    return 
end subroutine calculate