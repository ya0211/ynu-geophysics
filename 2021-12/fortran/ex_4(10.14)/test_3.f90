program test3
    implicit none
    integer n

    write(*,*) 'enter the parameters'
    read(*,*) n
    call out(n)

end program test3

subroutine out(n)
    implicit none
    integer i,n
    do i = 1, n
        call system('echo "*\c" ')
    end do
end subroutine  out