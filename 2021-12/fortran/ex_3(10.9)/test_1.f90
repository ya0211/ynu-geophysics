program test1
    implicit none
    dimension num(10)
    real num
    real sum
    integer i

    sum = 0
    do i = 1, 10
        num(i) = i*2
        sum = sum+num(i)
    end do

    !write(*,*)  num
    write(*,*) 'SUM = ', sum
    
end program test1