(ns palindrome)

; Should return if a word, phrase or number is a palindrome or not
; Constraints:
;  * input is always non-empty
;  * punctuation and space should not be considered in the phrase
(defn palindrome? [input]
  (when (empty input)
    true)
  (let [first (first input)
        last  (last input)]
    (if (= first last)
      (recur palindrome? (drop 1 input) (drop-last 1 input))
      false)))


