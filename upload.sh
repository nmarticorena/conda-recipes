for file in output/**/*.conda; do
    binstar upload -u nmarticorena $file || true
done

