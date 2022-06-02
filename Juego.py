from enum import Flag
from re import S
import pygame,sys
import Mapa
import time
pygame.init()
''' Nombre Funcion: ayuda():
    Objetivo:Crear la ventana de ayuda para explicar funcionamiento del juego
    Parametros: No aplica
    Retorna:No aplica'''
def ayuda():#ventana de ayuda
    pantalla = pygame.display.set_mode(size=(900,500))
    Presentacion = pygame.image.load("Imagenes//Ayuda.png")
    pantalla.blit(Presentacion,(0,0))
    pygame.display.update()
    while True:
        for Eventos in pygame.event.get():
            if Eventos.type == pygame.QUIT:
                Menu()
        pass
''' Nombre Funcion: Menu():
    Objetivo:Crear la ventana de menu para acceder a el juego, ayuda y salir
    Parametros: No aplica
    Retorna:No aplica'''
def Menu(): 
    pantalla = pygame.display.set_mode(size=(900,500))
    Presentacion = pygame.image.load("Imagenes//Menu.png")
    pantalla.blit(Presentacion,(0,0))
    pygame.display.update()
    while True: 
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                exit()
            if events.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if x > 662 and x <800  and y > 325 and y <376:
                    Jugar()
                if x > 662 and x < 800 and y > 394 and y < 445:
                    ayuda()
''' Nombre Funcion: Jugar():
    Objetivo:Crear la ventana del juego
    Parametros: No aplica
    Retorna:No aplica'''
def Jugar():
    #Variable para detener el ciclo del juego
    GameOver=True
    #Definición de reloj
    clock=pygame.time.Clock()
    Black=(0,0,0)
    #Importa el mapa con la libreria Mapa.py
    Lista=Mapa.ImportarMapa()
    CordenadasMuros=Mapa.CordenadasMuros(Lista)
    CordenadasFondo=Mapa.CordenadasFondo(Lista)
    CordenadasPiso=Mapa.CordenadasPiso(Lista)
    #Multiplica las cordenadas de los objetos por 50 para que sean proporcionales
    for i in CordenadasMuros:
        i[0]=i[0]*50
        i[1]=i[1]*50
    for i in CordenadasFondo:
        i[0]=i[0]*50
        i[1]=i[1]*50
    for i in CordenadasPiso:
        i[0]=i[0]*50
        i[1]=i[1]*50
    #Genera cordenadas especiales como las de los enemigos punto donde finaliza el juego y potenciadores todos de forma aleatoria
    CordenadasEnemigos=Mapa.PosicionEnemigos(CordenadasPiso)
    PuntoSalida=Mapa.PuntoSalida(CordenadasPiso)
    PotenciadoresVelocidad= Mapa.PuntosPotenciadores(CordenadasPiso)
    PotenciadoresVida= Mapa.PuntosPotenciadores(CordenadasPiso)
    PotenciadorTiempo =Mapa.PuntosPotenciadores(CordenadasPiso)
    #Clase Jugador
    class Player(pygame.sprite.Sprite):
        #Define atributos del jugador
        def __init__(self):
            super().__init__()
            self.image=pygame.image.load("Imagenes//LinkAbajoEstatico.png")
            self.image.set_colorkey(Black)
            self.rect = self.image.get_rect()
        #Define las imagenes de movimiento hacia diferentes direcciones
        def ActualizarImagen(self,Direccion):
            if Direccion=="Derecha":
                self.image=pygame.image.load("Imagenes//LinkDerecha.png")
            if Direccion=="Izquierda":
                self.image=pygame.image.load("Imagenes//LinkIzquierda.png")
            if Direccion=="Abajo":
                self.image=pygame.image.load("Imagenes//LinkAbajo.png")
            if Direccion=="Arriba":
                self.image=pygame.image.load("Imagenes//LinkArriba.png")
        #Define las imagenes de movimiento para crear la ilusion de movimiento animado
        def ActualizarImagen2(self,Direccion):    
            if Direccion=="Derecha":
                self.image=pygame.image.load("Imagenes//LinkDerecha1.png")
            if Direccion=="Izquierda": 
                self.image=pygame.image.load("Imagenes//LinkIzquierda1.png")
            if Direccion=="Abajo":
                self.image=pygame.image.load("Imagenes//LinkAbajo1.png")
            if Direccion=="Arriba":
                self.image=pygame.image.load("Imagenes//LinkArriba1.png")
        #Define las imagenes estaticas para cuando el jugador se queda quieto
        def ActualizarImagenEstatico(self,Direccion):    
            if Direccion=="Derecha":
                self.image=pygame.image.load("Imagenes//LinkDerechaEstatico.png")
            if Direccion=="Izquierda": 
                self.image=pygame.image.load("Imagenes//LinkIzquierdaEstatico.png")
            if Direccion=="Abajo":
                self.image=pygame.image.load("Imagenes//LinkAbajoEstatico.png")
            if Direccion=="Arriba":
                self.image=pygame.image.load("Imagenes//LinkArribaEstatico.png")
    #--------------------------------------------------------------------------------------------------
    #Clase Muros 
    class Muros(pygame.sprite.Sprite):
        #Define los atributos de los muros
        def __init__(self):
            super().__init__()
            self.image=pygame.image.load("Imagenes//Muro.png")
            self.image.set_colorkey(Black)
            self.rect = self.image.get_rect()

    #-------------------------------------------------------------------------------------------------
    #Clase Fondo juego
    class MuroFondo(pygame.sprite.Sprite):
        #Define los atributos de los bloques del fondo 
        def __init__(self):
            super().__init__()
            self.image=pygame.image.load("Imagenes//MuroFondo.png")
            self.image.set_colorkey(Black)
            self.rect = self.image.get_rect()
    #-------------------------------------------------------------------------------------------------
    #Piso juego
    class Piso(pygame.sprite.Sprite):
        #Define los atributos del piso del juego 
        def __init__(self):
            super().__init__()
            self.image=pygame.image.load("Imagenes//Piso.png")
            self.image.set_colorkey(Black)
            self.rect = self.image.get_rect()
    #-----------------------------------------------------------------------------------------------
    #Clase vidas
    class Vidas(pygame.sprite.Sprite):
        #Define los atributos de las vidas del jugador
        def __init__(self):
            super().__init__()
            self.image=pygame.image.load("Imagenes//VidaCompleta.png")
            self.image.set_colorkey(Black)
            self.rect = self.image.get_rect()
        #permite actualizar las vidas graficamente
        def ActualizarVidas(self,CantidadCorazones):
            if CantidadCorazones==3:
                self.image=pygame.image.load("Imagenes//VidaCompleta.png")
            if CantidadCorazones==2:
                self.image=pygame.image.load("Imagenes//VidaMedia.png")
            if CantidadCorazones==1:
                self.image=pygame.image.load("Imagenes//PocaVida.png")
    #------------------------------------------------------------------------------------------------
    #clase punto de salida o finalizacion
    class Salida(pygame.sprite.Sprite):
        #Define los atributos del punto donde finaliza el juego
        def __init__(self):
            super().__init__()
            self.image=pygame.image.load("Imagenes//Salida.png")
            self.image.set_colorkey(Black)
            self.rect = self.image.get_rect()

    #-------------------------------------------------------------------------------------------------
    #Clase enemigos
    class Enemigos(pygame.sprite.Sprite):
        #Define los atributos de los enemigos
        def __init__(self):
            super().__init__()
            self.image=pygame.image.load("Imagenes//Fantasma1.png")
            self.image.set_colorkey(Black)
            self.rect = self.image.get_rect()
    #--------------------------------------------------------------------------------------------------
    #Clase Rayo potenciador velocidad
    class RayoVelocidad(pygame.sprite.Sprite):
        #Define los atributos del potenciador de velocidad
        def __init__(self):
            super().__init__()
            self.image=pygame.image.load("Imagenes//Velocidad.png")
            self.image.set_colorkey(Black)
            self.rect = self.image.get_rect()
    #--------------------------------------------------------------------------------------
    #Corazon aumentavida
    class CorazonVida(pygame.sprite.Sprite):
        #Define los atributos del potenciador que aumenta la vida del jugador
        def __init__(self):
            super().__init__()
            self.image=pygame.image.load("Imagenes//MasVida.png")
            self.image.set_colorkey(Black)
            self.rect = self.image.get_rect()
    #--------------------------------------------------------------------------------------
    #Reloj aumenta tiempo
    class RelojTiempo(pygame.sprite.Sprite):
        #Define los atributos del objeto que aumenta el tiempo jugable
        def __init__(self):
            super().__init__()
            self.image=pygame.image.load("Imagenes//MasTiempo.png")
            self.image.set_colorkey(Black)
            self.rect = self.image.get_rect()
    #Cantidad Corazones
    CantidadCorazones=3
    #Inicializa la velocidad del jugador
    x_velocidad=0
    y_velocidad=0
    #-----------------------------------------------------------------------------------------------------------------------
    #se instancia cada uno de los objetos y se agregan a las listas de los sprites
    #Lista Jugadores
    JugadorLista=pygame.sprite.Group()
    Player=Player()
    Player.rect.x=450
    Player.rect.y=250
    JugadorLista.add(Player)
    #lista Muros
    MurosLista =pygame.sprite.Group()
    for i in CordenadasMuros:
        Muro=Muros()
        Muro.rect.x=i[0]
        Muro.rect.y=i[1]
        MurosLista.add(Muro)
    #Fondo muros
    FondoLista =pygame.sprite.Group()
    for i in CordenadasFondo:
        MuroF=MuroFondo()
        MuroF.rect.x=i[0]
        MuroF.rect.y=i[1]
        FondoLista.add(MuroF)
    #pisos 
    PisoLista =pygame.sprite.Group()
    for i in CordenadasPiso:
        Pisos=Piso()
        Pisos.rect.x=i[0]
        Pisos.rect.y=i[1]
        PisoLista.add(Pisos)
    #Corazones de vida
    CorazonesLista =pygame.sprite.Group()
    Vida=Vidas()
    Vida.rect.x=10
    Vida.rect.y=10
    CorazonesLista.add(Vida)
    #Punto de Salida
    SalidaLista=pygame.sprite.Group()
    Salidas=Salida()
    Salidas.rect.x=PuntoSalida[0]
    Salidas.rect.y=PuntoSalida[1]
    SalidaLista.add(Salidas)
    #Enemigos
    EnemigoLista =pygame.sprite.Group()
    for i in CordenadasEnemigos:
        Enemigo=Enemigos()
        Enemigo.rect.x=i[0]
        Enemigo.rect.y=i[1]
        EnemigoLista.add(Enemigo)
    #Rayo aumeta velocidad
    VelocidadLista = pygame.sprite.Group()
    for i in PotenciadoresVelocidad:
        RayoPotenciador=RayoVelocidad()
        RayoPotenciador.rect.x=i[0]
        RayoPotenciador.rect.y=i[1]
        VelocidadLista.add(RayoPotenciador)
    #Corazon Potenciador de vida
    AumentarVidaLista=pygame.sprite.Group()
    for i in PotenciadoresVida:
        CorazonPotenciador=CorazonVida()
        CorazonPotenciador.rect.x=i[0]
        CorazonPotenciador.rect.y=i[1]
        AumentarVidaLista.add(CorazonPotenciador)
    #Reloh aumenta el tiempo
    AumentarTiempoLista=pygame.sprite.Group()
    for i in PotenciadorTiempo:
        Reloj=RelojTiempo()
        Reloj.rect.x=i[0]
        Reloj.rect.y=i[1]
        AumentarTiempoLista.add(Reloj)
    #------------------------------------------------------------------------------------------------------------------------
    #Distancia a la que el enemigo te ve 
    DistanciaAccionEnemigo=300
    #Direccion de movimiento
    Direccion=""
    pygame.init()
    size=(900,500)
    screen = pygame.display.set_mode(size)
    #Inicia la musica de fondo
    file = 'Musica//Mistery.wav'
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(-1)
    #Iniciar de nuevo variable
    IniciardeNuevo=False
    Velocidad=3
    #Contador de  tiempo
    counter, text = 100,'100'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consolas', 30)
    TiempoHabilidadVelocidad=0
    FlagSonido=False
    print("Jugador :",Player.rect.x/50,"  ",Player.rect.y/50)
    print("Salida  :",Salidas.rect.x/50,"  ",Salidas.rect.y/50)
    #variables para el movimiento
    FlagMovimiento=True
    ContadorFrames=0
    DetenerMovimiento=True
    BotonesPresionados=0
    #Ciclo juego
    #---------------------------------------------------------------------
    while GameOver:
        #vuelve la velocidad a la normalidad
        if TiempoHabilidadVelocidad<1:
            Velocidad=3
        #Detien al jugador cuando choca con las paredes
        if pygame.sprite.spritecollideany(Player,MurosLista):
            x_velocidad=0
            y_velocidad=0
        #Detecta que se presionen las teclas
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.USEREVENT: 
                counter -= 1
                text = str(counter).rjust(3) if counter > 0 else 'boom!'
                if TiempoHabilidadVelocidad>0:
                    TiempoHabilidadVelocidad-=1
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_velocidad=-1*Velocidad
                    Direccion="Izquierda"
                    BotonesPresionados+=1
                if event.key==pygame.K_RIGHT:
                    x_velocidad=Velocidad
                    Direccion="Derecha"
                    BotonesPresionados+=1
                if event.key==pygame.K_UP:
                    y_velocidad=-1*Velocidad
                    Direccion="Arriba"
                    BotonesPresionados+=1
                if event.key==pygame.K_DOWN:
                    y_velocidad=Velocidad
                    Direccion="Abajo"
                    BotonesPresionados+=1                
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT:
                    x_velocidad=0
                    BotonesPresionados-=1
                if event.key==pygame.K_RIGHT:
                    x_velocidad=0
                    BotonesPresionados-=1
                if event.key==pygame.K_UP:
                    y_velocidad=0
                    BotonesPresionados-=1
                if event.key==pygame.K_DOWN:
                    y_velocidad=0
                    BotonesPresionados-=1
                DetenerMovimiento=False
        screen.fill(Black)
        if BotonesPresionados>0:
            DetenerMovimiento=True
        elif BotonesPresionados==0:
            DetenerMovimiento=False
        #Movimiento de todo el entorno para crear la ilusión de movimiento de los personajes
        for i in MurosLista:
            i.rect.y+=y_velocidad*-1
            i.rect.x+=x_velocidad*-1
        for i in FondoLista:
            i.rect.y+=y_velocidad*-1
            i.rect.x+=x_velocidad*-1
        for i in PisoLista:
            i.rect.y+=y_velocidad*-1
            i.rect.x+=x_velocidad*-1
        for i in EnemigoLista:
            i.rect.y+=y_velocidad*-1
            i.rect.x+=x_velocidad*-1
        for i in SalidaLista:
            i.rect.y+=y_velocidad*-1
            i.rect.x+=x_velocidad*-1
        for i in VelocidadLista:
            i.rect.y+=y_velocidad*-1
            i.rect.x+=x_velocidad*-1
        for i in AumentarVidaLista:
            i.rect.y+=y_velocidad*-1
            i.rect.x+=x_velocidad*-1
        for i in AumentarTiempoLista:
            i.rect.y+=y_velocidad*-1
            i.rect.x+=x_velocidad*-1
        #Movimiento de los enemigos para que persigan al jugador
        for i in EnemigoLista:
            if DistanciaAccionEnemigo>abs(i.rect.y-Player.rect.y) and DistanciaAccionEnemigo>abs(i.rect.x-Player.rect.x):
                if i.rect.y > Player.rect.y:
                    i.rect.y-=1
                else:
                    i.rect.y+=1
                if i.rect.x > Player.rect.x:
                    i.rect.x-=1
                else:
                    i.rect.x+=1
        #Colisión del jugador con todos los enemigos
        if pygame.sprite.spritecollide(Player,EnemigoLista,True):
            CantidadCorazones=CantidadCorazones-1
            pygame.mixer.Sound("Musica//Fantasma.wav").play()
            if CantidadCorazones<=0:
                GameOver=False
                FlagSonido=False
                pygame.mixer.music.stop()
                pygame.mixer.Sound("Musica//lose.mp3").play()
                pantalla = pygame.display.set_mode(size=(900,500))
                Presentacion = pygame.image.load("Imagenes//Lose.png")
                pantalla.blit(Presentacion,(0,0))
                pygame.display.update()
                time.sleep(5)
                IniciardeNuevo=True
            else:
                Vida.ActualizarVidas(CantidadCorazones)
        #Colisión del jugador el punto de salida o finalizar
        if pygame.sprite.spritecollideany(Player,SalidaLista):
            GameOver=False
            pygame.mixer.music.stop()
            FlagSonido=False
            pantalla = pygame.display.set_mode(size=(900,500))
            pygame.mixer.Sound("Musica//Win.mp3").play()
            Presentacion = pygame.image.load("Imagenes//Win.png")
            pantalla.blit(Presentacion,(0,0))
            pygame.display.update()
            time.sleep(5)
            IniciardeNuevo=True
        #Muestra la pantalla de perdida si se acaba el tiempo
        if counter==0:
            FlagSonido=False
            pygame.mixer.music.stop()
            pygame.mixer.Sound("Musica//lose.mp3").play()
            GameOver=False
            pantalla = pygame.display.set_mode(size=(900,500))
            Presentacion = pygame.image.load("Imagenes//Lose.png")
            pantalla.blit(Presentacion,(0,0))
            pygame.display.update()
            time.sleep(5)
            IniciardeNuevo=True
        #Colisión del jugador con el potenciador RAYO que aumenta la velocidad
        if pygame.sprite.spritecollide(Player,VelocidadLista,True):
            Velocidad=6
            TiempoHabilidadVelocidad=30
            pygame.mixer.Sound("Musica//Plus.wav").play()
            file = 'Musica//sweetdreams.mp3'
            pygame.mixer.music.set_volume(0.3)
            pygame.mixer.init()
            pygame.mixer.music.load(file)
            pygame.mixer.music.play(1)
            FlagSonido=True
        #Quita la musica especial para cuando tiene super velocidad
        if TiempoHabilidadVelocidad==0 and FlagSonido:
            file = 'Musica//Mistery.wav'
            pygame.mixer.init()
            pygame.mixer.music.load(file)
            pygame.mixer.music.play(-1)
            FlagSonido=False
        #Colision con los corazones que aumentan la vida del jugador 
        if pygame.sprite.spritecollide(Player,AumentarVidaLista,True):
            pygame.mixer.Sound("Musica//Plus.wav").play()
            if CantidadCorazones<3:
                CantidadCorazones+=1
                Vida.ActualizarVidas(CantidadCorazones)
        #Colision del jugador con los relojes que aumentan el tiempo
        if pygame.sprite.spritecollide(Player,AumentarTiempoLista,True):
            pygame.mixer.Sound("Musica//Plus.wav").play()
            counter+=30
        #contador de frames para la animacion del movimiento
        ContadorFrames+=1
        if ContadorFrames%17==0:
            if FlagMovimiento:
                FlagMovimiento=False
            else:
                FlagMovimiento=True
            if not DetenerMovimiento:
                Player.ActualizarImagenEstatico(Direccion)
            else:
                if FlagMovimiento:
                    Player.ActualizarImagen(Direccion)
                else:
                    Player.ActualizarImagen2(Direccion)
        #Dibujar todos los sprites
        MurosLista.draw(screen)
        PisoLista.draw(screen)
        FondoLista.draw(screen)
        JugadorLista.draw(screen)
        SalidaLista.draw(screen)
        VelocidadLista.draw(screen)
        AumentarVidaLista.draw(screen)
        AumentarTiempoLista.draw(screen)
        EnemigoLista.draw(screen)
        CorazonesLista.draw(screen)
        #dibujar cronometro
        screen.blit(font.render(text, True, (255, 255, 255)), (830,10))
        pygame.display.flip()
        pygame.mixer.music.unpause()
        clock.tick(60)
    #inicializa el juego cuando pierde o gana
    if IniciardeNuevo:
            Menu()
Menu()