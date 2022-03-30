program test3
    implicit none
    integer i,n
    parameter(n=10)
    dimension name(n),s(n)
    character name*10
    real s

    open(1, file = 'stu1.txt')
    open(2, file = 'stu2.txt')
    
    do i = 1,n
        read(1,*) name(i),s(i)
        !write(*,*) name(i),s(i)
        s(i)=sqrt(s(i))*10
        !write(*,*) name(i),s(i)
        !write(*,*) ' '
        write(2,*) name(i),s(i)
    end do

    close(1)
    close(2)
end program test3