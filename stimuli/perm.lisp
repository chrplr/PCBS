;; random shuffle of the rows of a csv file

;;

(uiop:command-line-arguments)

;;

(ql:quickload 'read-csv)
(use-package :read-csv)

(defun repeat (x y)
  (if (zerop y)
      nil
      (cons x
            (repeat x (1- y)))))

(defun nshuffle (sequence)
  (loop for i from (length sequence) downto 2
        do (rotatef (elt sequence (random i))
                    (elt sequence (1- i))))
  sequence)


(defvar p "/home/cp983411/anovas-bert.csv")
(defvar data (repeat (with-open-file (s P) (parse-csv s)) 1000))

(time (nshuffle data))


