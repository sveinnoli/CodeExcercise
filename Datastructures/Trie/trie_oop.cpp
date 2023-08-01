#include <unordered_map>
#include <vector>
#include <iostream>
#include <string>

class TrieNode {
public:
    std::unordered_map<char, TrieNode*> children;
    bool is_end_of_word;
};

class Trie {
public:
    TrieNode* root = new TrieNode();

    void insert(std::string& str) {
        TrieNode* current = root;
        
        for (char c : str) {
            if (current->children.find(c) == current->children.end()) {
                current->children[c] = new TrieNode();
            }
            current = current->children[c];
        }
        current->is_end_of_word = true;
    }

    std::string shortestPrefixOfWord(std::string word) {
        TrieNode* current = this->root;
        for (int i = 0; i < word.length(); i++) {
            if (current->is_end_of_word || current->children.size() > 1) {
                word.resize(i);
                break;
            }
            current = current->children[word[i]];
        }
        return word;
    }
};
