#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

class Player {
public:
    string name;
    int health;
    int attackPower;

    Player(string n, int h, int a) : name(n), health(h), attackPower(a) {}

    void attack(Player &opponent) {
        int damage = rand() % attackPower + 1;
        opponent.health -= damage;
        cout << name << " attacks " << opponent.name << " for " << damage << " damage!" << endl;
        if (opponent.health <= 0) {
            opponent.health = 0;
            cout << opponent.name << " has been defeated!" << endl;
        } else {
            cout << opponent.name << " has " << opponent.health << " health remaining." << endl;
        }
    }
};

int main() {
    srand(static_cast<unsigned int>(time(0)));

    string playerName;
    cout << "Enter your player's name: ";
    cin >> playerName;

    Player player1(playerName, 100, 20);
    Player player2("Enemy", 100, 15);

    cout << "Battle Start!" << endl;

    while (player1.health > 0 && player2.health > 0) {
        player1.attack(player2);
        if (player2.health <= 0) break;
        player2.attack(player1);
        if (player1.health <= 0) break;
        cout << "--------------------------------" << endl;
    }

    if (player1.health > 0) {
        cout << player1.name << " wins!" << endl;
    } else {
        cout << player2.name << " wins!" << endl;
    }

    return 0;
}
