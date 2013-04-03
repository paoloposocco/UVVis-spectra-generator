real function y_lorentz(x_current, x_center, fwhm)
     implicit none
     real, intent(in):: x_current, x_center, fwhm
     real, parameter::pi=3.141592526
     y_lorentz=(1.0/(pi))*0.5*fwhm/((x_current-x_center)**2.0+(0.5*fwhm)**2.0)
     write(*,*) 'y= ', y_lorentz
     return
     end function y_lorentz 
     ! per ora lavoriamo in nm
     ! e per la y?
real function y_lorentz2(x_current, x_center, fwhm, height)
     implicit none
     real, intent(in):: x_current, x_center, fwhm, height
     real, parameter::pi=3.141592526
     y_lorentz2=height/(1+((x_current-x_center)/fwhm)**2)
     !write(*,*) 'y= ', y_lorentz
     return
     end function y_lorentz2
! TO DO
     !una volta fatto cerca libreria che lo faccia x confronto
     !eventualment subroutine parser x leggere da dalton
program UV_fort
      implicit none
      integer::n, n_max, errore_io, step_number, i, j
      integer::allocate_status, lines
      real::min_window, max_window, step_width, y_threshold
      real:: x_current, y_current, y_lorentz, y_lorentz2
      !real array allocabile x lo spettro
      ! real array di input
      real, dimension(100:350,2):: spectrum
      real, dimension(:,:), allocatable:: input
      !input=(/(5.276733, 0.1299), (6.000544, 0.0321), (6.667589, 0.1031)/)
      !input=(/(5.276733, 6.000544, 6.667589), (0.1299, 0.0321, 0.1031)/)
      ! se mi accontento della precisione intera posso usare lo stesso valore
      ! come indice per x_center
      OPEN(UNIT=5 , FILE ='spectrum.out',STATUS='REPLACE', ACTION='WRITE',&
              &iostat=errore_io)
      OPEN(UNIT=3 , FILE ='input.txt',STATUS='old', ACTION='read',&
              &iostat=errore_io)
      write(*,*) 'scrivi numero linee input'
      !read(*,*) lines
      lines=3
      allocate (input(lines,2), stat= allocate_status)
      do i=1, lines
            read(3,*) input(i,1),input(i,2)
              write(*,*) 'input= ', input
            end do
      if (allocate_status/=0) STOP 'ERRORE ALLOCAZIONE MEMORIA'
      write(*,*) 'input= ', input
      input(1,1)=235
      input(1,2)=0.1299
      !input(1,2)=26
      input(2,1)=207
      input(2,2)=0.0321
      !input(2,2)=6.42
      input(3,1)=186
      input(3,2)=0.1031
      !input(3,2)=2.06
      write(*,*) 'input= ', input
      spectrum=0.0
      do i=350, 100, -1
            spectrum(i,1) = i
            end do 
      !write(*,*) 'spectrum= ', spectrum
      if(errore_io /= 0) stop 'errore scrittura file' !v. se controllare anche
      ! input
            write(*,*) 'tutot ok'
      do j=1,3
            do i=100, 350
                    spectrum(i,2)=spectrum(i,2)+10.0*y_lorentz2(real(i), input(j,1),2.95, input(j,2))
                    end do
            end do
      do i=100,350
                    write(5,*) spectrum(i,:)
                    end do
      stop
      end program UV_fort
