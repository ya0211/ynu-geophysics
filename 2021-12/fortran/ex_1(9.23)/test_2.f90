program test2
    implicit none
    integer num

    write(*,*)"Enter week number"
    read(*,*)num

    if(num==1.or.num==4)then
        write(*,*)"The show is news"
    else if(num==2.or.num==5)then
        write(*,*)"The show is a TV series"
    else if(num==3.or.num==6)then
        write(*,*)"The show is Cartoon" 
    else
        write(*,*)"The show is movie"
    endif

end