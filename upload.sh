for file in output/**/*.conda; do
    rattler-build upload anaconda -v -o nmarticorena $file || true
done

