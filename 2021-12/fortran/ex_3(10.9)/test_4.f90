program test4
    implicit none
    dimension a(10)
    integer a,c
    integer i,j

    a = (/5,3,6,4,8,7,1,9,2,10/)
    
    do i = 1, 9
        do j = i+1, 10
            if(a(j) > a(i))then
                c = a(i)
                a(i) =  a(j)
                a(j) = c
            end if
        end do
    end do

    write(*,*) a

end program test4