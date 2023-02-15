(ns palindrome)

; Should return if a word, phrase or number is a palindrome or not
; Constraints:
;  * input is always non-empty
;  * punctuation and space should not be considered in the phrase

(defn- next-input [input]
  (->> input
       (drop-last 1)
       (drop 1)
       (apply str)))

(defn is-it? [input]
  (if (< (count input) 2)
    true
    (if (= (first input) (last input))
      (is-it? (next-input input))
      false)))

(defn is-it-2? [input]
  (= input (->> input reverse (apply str))))



