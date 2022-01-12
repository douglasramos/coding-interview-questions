(ns validate-subsequence)

;; How can we avoid using index-of? take-while? for?

(defn valid-sequence? [sequence array]
  (loop [seq sequence
         arr array]
    (if (empty? seq)
      true
      (if-let [rest-array  (->> arr 
                            (drop-while (partial not= (first seq)))
                            rest)]
        (recur (rest seq) rest-array)
        false))))

(defn run []
  (println (valid-sequence? [1 3 4 5] [1 4 2 3 3 5])))

(run)

