source "https://rubygems.org"

# Jekyll version to run
gem "jekyll", "~> 4.3"

# Default theme for Jekyll sites
gem "minima", "~> 2.0"

gem "kramdown-parser-gfm"

# Uncomment the following line if you're using GitHub Pages
# gem "github-pages", group: :jekyll_plugins

# Adding Bootstrap for styling
gem "bootstrap", "~> 5.1.3"

# Plugins for Jekyll
group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.6"
  gem "jekyll-paginate"
end

# Windows-specific gems
install_if -> { RUBY_PLATFORM =~ %r!mingw|mswin|java! } do
  gem "tzinfo", "~> 1.2"
  gem "tzinfo-data"
end

# Performance booster for watching directories on Windows


# Required for Jekyll server
gem "webrick", "~> 1.7"

# Optional: Add `listen` gem to ensure compatibility
gem "listen", "~> 3.3"

gem "logger"
