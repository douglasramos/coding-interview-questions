(ns palindrome-test
  (:require [clojure.test :refer :all]
            [palindrome :as palindrome]))

(deftest palindrome-test
  (testing "palindromes"
    (are [input]
         (true? (palindrome/is-it? input))
      "obo"
      "b"
      ""
      "oaqqao"
      "wwaaww"
      "wxyxw"
      "aaxyyxaa"))

  (testing "not palindromes"
    (are [input]
         (false? (palindrome/is-it? input))
      "oba"
      "ba"
      "obqqao"
      "wwaawz"
      "wxysaxw"
      "aqxyyvaa")))

(deftest alternative-palindrome-test
  (testing "palindromes"
    (are [input]
         (true? (palindrome/is-it-2? input))
      "obo"
      "b"
      ""
      "oaqqao"
      "wwaaww"
      "wxyxw"
      "aaxyyxaa"))

  (testing "not palindromes"
    (are [input]
         (false? (palindrome/is-it-2? input))
      "oba"
      "ba"
      "obqqao"
      "wwaawz"
      "wxysaxw"
      "aqxyyvaa")))