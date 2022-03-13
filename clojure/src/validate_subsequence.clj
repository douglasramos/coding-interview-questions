(ns validate-subsequence)

(defn subsequence? [seq array]
  (if (empty? seq)
    true
    (let [sub-arr (->> array
                     (drop-while (partial not= (first seq))))]
      (if (not-empty sub-arr)
        (recur (rest seq) (rest sub-arr))
        false))))

(defn run []
  ;; true
  (println (subsequence? [1 2 3] [-1 1 4 10 0 25 1 3])))

