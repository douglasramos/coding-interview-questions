(ns validate-subsequence-test
  (:require [clojure.test :refer :all]
            [validate-subsequence :as validate]))

(deftest validate-subsequence-test
  (testing "subsequences"
    (are [seq arr]
      (true? (validate/subsequence? seq arr))
      [1 2 3] [-1 1 4 10 2 25 1 3]
      [3] [3]
      [4 5 6] [1 2 6 4 5 6]
      [3] [4 3 5]))

  (testing "not subsequences"
    (are [seq arr]
      (false? (validate/subsequence? seq arr))
      [1 2 3] [-1 1 4 10 0 25 1 3]
      [3] [4]
      [3] [0 1 2]
      [4 5 6] [1 2 3 6 5 6])))