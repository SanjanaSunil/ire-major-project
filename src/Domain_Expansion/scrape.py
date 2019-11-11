# working urls - https://bharatswasthya.net/body-science/
# https://bharatswasthya.net/eye-ear/
# url = 'https://bharatswasthya.net/itchy-bimariya/
# url = 'https://bharatswasthya.net/jua/'
# 'https://bharatswasthya.net/khujli-shortarticle/'
# 'https://bharatswasthya.net/reproduction/#rescue-skin-immune'
# https://bharatswasthya.net/cells-tissue-fluid/
# https://bharatswasthya.net/reproduction/
# https://bharatswasthya.net/digestive-respiratory/
# https://bharatswasthya.net/brain-nerves-hormone/
# https://bharatswasthya.net/cells-tissue-fluid/#genetics
# https://bharatswasthya.net/digestive-respiratory/#respiratory-system
# https://bharatswasthya.net/bone-cells/
# https://bharatswasthya.net/common-fracture/
# https://bharatswasthya.net/rheumatic-arthritis-2/
# https://bharatswasthya.net/bones-transition/
# https://bharatswasthya.net/spondylitis/
# https://bharatswasthya.net/gardan-dard-shortarticle-2/
# https://bharatswasthya.net/bone-cancer/
# https://bharatswasthya.net/joints-illnesses-2/
# https://bharatswasthya.net/kamar-dard-shortarticle/
# https://bharatswasthya.net/fracture-classification-2/
# https://bharatswasthya.net/joints-sprain/
# https://bharatswasthya.net/preventinglower-backpain-shortarticle/
# https://bharatswasthya.net/digestion-technique/
# http://www.hinditechy.com/10-must-know-excel-formulas-hindi/
# http://www.hinditechy.com/tor-browser-hindi-hide-ip-address/
# https://www.techactive.in/what-is-website-in-hindi/
# https://www.techactive.in/build-high-quality-backlinks/
# https://www.techactive.in/off-page-seo-in-hindi/
# https://www.techactive.in/best-wordpress-plugins-in-hindi/
# https://www.techactive.in/movierulz-movies-download-hindi/
# https://www.techactive.in/freelancing-in-hindi-and-earn-money/
# https://www.techactive.in/business-income-increase-with-digital-marketing/
# https://www.techactive.in/what-is-a-blog-in-hindi-difference-between-website-and-blog/
# https://www.techactive.in/what-is-google-firebase/
# https://www.techactive.in/best-wordpress-themes-for-hindi-blogger/
# https://www.techactive.in/best-wordpress-plugins-in-hindi/
# https://www.techactive.in/9xmovies-movies-download-hindi/
# https://www.techactive.in/sarkari-naukri-government-jobs-latest-update/
# https://www.techactive.in/what-is-jiofiber-in-hindi/
# https://www.techactive.in/5-best-travel-apps-that-every-traveler-should-have-in-their-smartphone/
import newspaper
from newspaper import Article

# url = 'https://www.techactive.in/what-is-jiofiber-in-hindi/'
url = 'https://www.techactive.in/5-best-travel-apps-that-every-traveler-should-have-in-their-smartphone/'

sina_paper = newspaper.build(url, language='hi')

all_urls = []
all_urls.append(url)
for category in sina_paper.category_urls():
    all_urls.append(category)
# article = sina_paper.articles[0]
# article.download()
# article.parse()
# print(article)
print(all_urls)

for i in all_urls:
	a = Article(i, language='hi') # Chinese
	a.download()
	a.parse()
	strr = './data/' + a.title + '.txt'
	file1 = open(strr,"w") 
	file1.write(a.text) 
	file1.close()