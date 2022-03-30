program a6
    implicit none
    integer, parameter :: row = 2
    integer, parameter :: col = 2
    !integer :: a(2,2)=(/1,2,3,4/)
    integer :: a(2,2)
    
    ! a(1, 1) = 1, a(2, 1) = 2, a(1, 2) = 3, a(2, 2) = 4
    
    integer :: b(4)=(/5,6,7,8/)
    integer :: c(2)
    
    a=reshape((/1,2,3,4/), (/2,2/))
    
    write(*,*) a
    write(*,*) a(:,1)
    c = a(:,1)
    write(*,*) c
    c = a(2,:)
    write(*,*) c
    write(*,*) c(2:1:-1)
    c = b(1:4:2) 
    write(*,*) c
    
    stop
    
    end