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
};


class Solution {
public:
    std::string longestCommonPrefix(std::vector<std::string>& strs) {
        Trie trie = Trie();
        for (std::string s : strs) {
            trie.insert(s);
        }

        TrieNode* current = trie.root;
        std::string randoword = strs[0];
        for (int i = 0; i < randoword.length(); i++) {
            if (current->is_end_of_word || current->children.size() > 1) {
                randoword.resize(i);
                break;
            }
            current = current->children[randoword[i]];
        }
        return randoword;
    }
};


int main(int argc, char** argv) {
    std::vector<std::string> v;
    Solution s;
    v.push_back("streot");
    v.push_back("streat");
    v.push_back("street");
    std::cout << s.longestCommonPrefix(v) << std::endl;
    return 0;
};