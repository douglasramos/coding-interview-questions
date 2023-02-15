(ns validate-subsequence)

(defn subsequence? [seq array]
  (if (empty? seq)
    true
    (let [sub-arr (->> array
                       (drop-while (partial not= (first seq))))]
      (if (not-empty sub-arr)
        (recur (rest seq) (rest sub-arr))
        false))))
