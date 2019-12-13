#include <cstdio>
#include <random>
#include <cmath>
#define PI 4*atan(1) //aproximação para PI

//Funcao trasformada com coordenadas polares
double funcao(double r, double theta){
    return 2*(((4-pow(r, 2))*sqrt(3)*pow(r, 2)));
}

//Funcao Um Terco de Simpson para 2D
double umTerco2D(int n, double h1, double h2, double lInferiorR, double lInferiorTheta){
    double integral = 0;

    for(int i=0; i<n-1; i+=2){
        for(int j=0; j<n-1; j+=2){
            integral += 2*(h2)*2*(h1)*(funcao(lInferiorR + h1*j, lInferiorTheta + h1*j) +
            4*funcao(lInferiorR + h1*(j+1), lInferiorTheta + h1*(j+1)) +
            funcao(lInferiorR + h1*(j+2), lInferiorTheta + h1*(j+2)))/6;
        }
    }

    return integral;
}

//Funcao Tres Oitavos de Simpson para 2D
double tresOitavos2D(int n, double h1, double h2, double lInferiorR, double lInferiorTheta){
    double integral = 0;

    for(int i=0; i<n-1; i+=3){
        for(int j=0; j<n-1; j+=3){
            integral += 3*h1*3*h2*(funcao(lInferiorR + h1*j, lInferiorTheta + h1*j) +
            3*funcao(lInferiorR + h1*(j+1), lInferiorTheta + (h1*(j+1))) +
            3*funcao(lInferiorR + h1*(j+2), lInferiorTheta + h1*(j+2)) +
            funcao(lInferiorR + h1*(j+3),lInferiorTheta + h1*(j+3)))/8;
        }
    }

    return integral;
}

//Funcao Regra de Boole para 2D
double regraDeBoole(int n, double h1, double h2, double lInferiorR, double lInferiorTheta){
    double integral = 0;

    for(int i=0; i<n-1; i+=4){
        for(int j=0; j<n-1; j+=4){
            integral += 4*h1*4*h2*(7*funcao(lInferiorR + h1*j, lInferiorTheta + h1*j) +
            32*funcao(lInferiorR + h1*(j+1), lInferiorTheta + h1*(j+1)) +
            12*funcao(lInferiorR + h1*(j+2), lInferiorTheta + h1*(j+2)) +
            32*funcao(lInferiorR + h1*(j+3), lInferiorTheta + h1*(j+3)) +
            7*funcao(lInferiorR + h1*(j+4), lInferiorTheta + h1*(j+4)))/90;
        }
    }

    return integral;
}

//Funcao Regra de Seis Pontos para 2D
double regraSeisPontos(int n, double h1, double h2, double lInferiorR, double lInferiorTheta){
    double integral = 0;

    for(int i=0; i<n-1; i+=5){
        for(int j=0; j<n-1; j+=5){
            integral += 5*h1*5*h2*(19*funcao(lInferiorR + h1*j, lInferiorTheta + h1*j) +
            75*funcao(lInferiorR + h1*(j+1), lInferiorTheta + h1*(j+1)) +
            50*funcao(lInferiorR + h1*(j+2), lInferiorTheta + h1*(j+2)) +
            50*funcao(lInferiorR + h1*(j+3), lInferiorTheta + h1*(j+3)) +
            75*funcao(lInferiorR + h1*(j+4), lInferiorTheta + h1*(j+4)) +
            19*funcao(lInferiorR + h1*(j+5), lInferiorTheta + h1*(j+5)))/288;
        }
    }

    return integral;
}

int main(){
    //Limites de integracao
    double lInferiorR = 0, lSuperiorR = 2, lInferiorTheta = 0, lSuperiorTheta = 2*PI;

    //Numero de pontos
    int n = 901;

    //Tamanho do intervalo entre dois pontos nas duas dimensoes
    double h1 = (lSuperiorR-lInferiorR)/(n-1), h2 = (lSuperiorTheta-lInferiorTheta)/(n-1);

    printf("%f\n", umTerco2D(n, h1, h2, lInferiorR, lInferiorTheta));
    printf("%f\n", tresOitavos2D(n, h1, h2, lInferiorR, lInferiorTheta));
    printf("%f\n", regraDeBoole(n, h1, h2, lInferiorR, lInferiorTheta));
    printf("%f\n", regraSeisPontos(n, h1, h2, lInferiorR, lInferiorTheta));
}
