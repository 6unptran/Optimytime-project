from django.shortcuts import render
from django.http import JsonResponse
import google.generativeai as genai
import re
from time import strftime
import datetime
now = datetime.datetime.now()
from gtts import gTTS
from datetime import date
import requests
from time import strftime
from gtts import gTTS
# Create your views here.
genai.configure(api_key="AIzaSyDCyPuDPUOVj_nSlGK-pGqDgOeRtkZq9eo")
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")

def replace_gemini(text):
     return re.sub(r"Gemini","optimize",text)
def replace_google(text):
     return re.sub(r"Google","một nhóm học sinh",text)




def home(request):
    return render(request, 'home.html')


def requests_msg(request):
    _input = request.GET.get('hehe')
    if "phương pháp học tập" in _input:
        output=f"""
Đây là một số phương pháp học tập tôi đề xuất cho bạn giúp học tập hiệu quả hơn 
\n
I.Phương pháp Active Recall (Chủ động gợi nhớ):
\n
Là một kỹ thuật học tập mạnh mẽ, dựa trên việc chủ động truy xuất thông tin từ trí nhớ để cải thiện khả năng ghi nhớ và hiểu biết. Đây là cách học thông qua tự kiểm tra, thay vì chỉ đọc lại nội dung. Phương pháp này thường được áp dụng thông qua việc sử dụng flashcards hoặc tự tạo câu hỏi.
\n
CÁC BƯỚC THỰC HIỆN: 
\n
Bước 1.Tự hỏi và trả lời về kiến thức đã học.   
\n
Bước 2.Sử dụng flashcards để gợi nhớ thông tin.
\n
Bước 3.Lập sơ đồ tư duy (mindmap) để hệ thống hóa kiến thức.
\n
Bước 4.Làm bài tập và thực hành nói to (verbalize) kiến thức.
\n
Bước 5.Truyền đạt lại kiến thức cho người khác.
\n
II.Phương pháp Pomodoro:
\n
Khi bạn không thể tập trung học quá 15 phút hoặc để quản lý thời gian, cải thiện sự tập trung và giảm thiểu sự phân tâm của người học.
\n
CÁC BƯỚC THỰC HIỆN: 
Bước 1. Chọn một công việc bất kỳ mà bạn cần thực hiện. Dù là việc to hay việc nhỏ, bạn cũng nên dành trọn sự tập trung và năng lượng của bản thân để làm việc.
\n
Bước 2: Đặt báo thức với khoảng thời gian phù hợp, thông thường là khoảng 25 phút.
\n
Bước 3: Làm việc cho đến khi hết thời gian, không để ngoại cảnh tác động lên bản thân.
\n
Bước 4: Khi hoàn thành 1 Pomodoro, bạn có thể nghỉ ngơi trong 5 phút và nên tận hưởng khoảng thời gian quý giá này.
Bước 5: Sau 4 lần nghỉ giải lao, bạn có thể nghỉ dài hơn với thời gian 10, 15 hay 30 phút tùy vào tình trạng mỗi người
\n
III. Phương pháp học Feynman:
\n
 Là một phương pháp học tập hiệu quả giúp chúng ta hiểu sâu về kiến thức. Bằng cách đóng vai là “giáo viên” giảng bài cho người khác một cách đơn giản và rõ ràng, chúng ta phát hiện những lỗ hổng trong kiến thức của mình. Sau đó, chúng ta tìm hiểu thêm về thông tin để giải thích một cách rõ ràng và chính xác. Quá trình này giúp củng cố và ghi nhớ kiến thức một cách hiệu quả. 
\n
CÁC BƯỚC THỰC HIỆN:
Bước 1: Đọc, nghiên cứu ban đầu: Để bắt đầu, hãy xác định một chủ đề mà người học cần học, đặc biệt chọn những lĩnh vực thiên về lý thuyết. Nghiên cứu những tài liệu, giáo trình liên quan để có một nền tảng kiến thức ổn định.  Cần thực sự đi sâu vào trọng tâm chứ không phải đọc lướt qua văn bản. Một mẹo nhỏ nên áp dụng là hãy giải thích từng dòng khi đọc bởi cách này cho phép bạn hiểu rõ khái niệm ngay trong quá trình học và ghi nhớ nhanh chóng hơn.
\n
Bước 2: Viết và giải thích lại: Sau khi đã đọc và ngâm cứu các thông tin thì chuẩn bị một tờ giấy và viết về chủ đề đó bằng những gì mình hiểu. Không cần quan trọng đã đầy đủ hay đúng trình tự hay chưa, chỉ cần liệt kê tất cả nội dung bản thân tiếp nhận được và định nghĩa lại bằng các thuật ngữ cơ bản nhất, kèm theo đó là những ví dụ minh họa. Ngoài ra, bạn cũng có thể thử dạy cho những người thân xung quanh để nhận được những phản ứng thực tế từ họ. Những lời góp ý cùng những câu hỏi của đối phương sẽ giúp ta học hỏi, rèn giũa tư duy hơn. Không những vậy, việc giảng dạy sẽ rèn luyện sự tự tin, sự trôi chảy mạch lạc khi giao tiếp và tích lũy vốn ngôn ngữ
\n
Bước 3: Xác định những lỗ hổng kiến thức: Đối với bước này, việc phát hiện và rà soát kỹ lưỡng những vấn đề còn nhầm lẫn hay bỏ sót là hết sức quan trọng. Liệu các ý tưởng, khía cạnh vừa đưa ra đã thực sự gãy gọn, rõ ràng vào thấu đáo hay chưa? Tiếp theo là dành thời gian quay lại và tìm hiểu lại các tài liệu học tập, đặc biệt chú ý tới những phần chưa hiểu. Lấp đầy những khoảng trống kiến thức là một cách để mở rộng vốn hiểu biết của bản thân. Thực tế cho thấy, khi con người học càng nhiều thì năng lực tiếp thu càng tăng lên. 
"""
    else:  
        result = model.generate_content(_input)
        text1=replace_gemini(result.text)
        text2=replace_google(text1)
        output=text2
    return JsonResponse({'message': output.replace("\n","<br>").replace("*","").replace("#","")})  