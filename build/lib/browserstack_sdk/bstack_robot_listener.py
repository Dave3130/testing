# coding: UTF-8
import sys
bstack111l11_opy_ = sys.version_info [0] == 2
bstack111ll1l_opy_ = 2048
bstack1_opy_ = 7
def bstack11111_opy_ (bstack1l111ll_opy_):
    global bstack111ll11_opy_
    bstack1lllll_opy_ = ord (bstack1l111ll_opy_ [-1])
    bstack1l1llll_opy_ = bstack1l111ll_opy_ [:-1]
    bstack11l11l_opy_ = bstack1lllll_opy_ % len (bstack1l1llll_opy_)
    bstack111l_opy_ = bstack1l1llll_opy_ [:bstack11l11l_opy_] + bstack1l1llll_opy_ [bstack11l11l_opy_:]
    if bstack111l11_opy_:
        bstack1l1l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1l1l1l_opy_ = str () .join ([chr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1l1l1l_opy_)
import os
import threading
from uuid import uuid4
from itertools import zip_longest
from collections import OrderedDict
from robot.libraries.BuiltIn import BuiltIn
from browserstack_sdk.bstack1ll1ll1l_opy_ import RobotHandler
from bstack_utils.capture import bstack1lllll11_opy_
from bstack_utils.bstack1ll1ll11_opy_ import bstack1ll11ll1_opy_, bstack1l11l1ll_opy_, bstack1ll1111l_opy_
from bstack_utils.bstack1l1lll11_opy_ import bstack11llll11_opy_
from bstack_utils.bstack1llll1ll_opy_ import bstack1l11lll1_opy_
from bstack_utils.constants import *
from bstack_utils.helper import bstack1l1lllll_opy_, bstack1l11llll_opy_, Result, \
    error_handler, bstack1l1111l1_opy_
class bstack_robot_listener:
    ROBOT_LISTENER_API_VERSION = 2
    _lock = threading.Lock()
    store = {
        bstack11111_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧࡶ"): [],
        bstack11111_opy_ (u"ࠫ࡬ࡲ࡯ࡣࡣ࡯ࡣ࡭ࡵ࡯࡬ࡵࠪࡷ"): [],
        bstack11111_opy_ (u"ࠬࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡴࠩࡸ"): []
    }
    bstack1llll111_opy_ = []
    bstack11lllll1_opy_ = []
    @staticmethod
    def bstack1l1lll1l_opy_(log):
        if not ((isinstance(log[bstack11111_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧࡹ")], list) or (isinstance(log[bstack11111_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨࡺ")], dict)) and len(log[bstack11111_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩࡻ")])>0) or (isinstance(log[bstack11111_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪࡼ")], str) and log[bstack11111_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫࡽ")].strip())):
            return
        active = bstack11llll11_opy_.bstack11lll1l1_opy_()
        log = {
            bstack11111_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪࡾ"): log[bstack11111_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫࡿ")],
            bstack11111_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩࢀ"): bstack1l1111l1_opy_().isoformat() + bstack11111_opy_ (u"࡛ࠧࠩࢁ"),
            bstack11111_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩࢂ"): log[bstack11111_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪࢃ")],
        }
        if active:
            if active[bstack11111_opy_ (u"ࠪࡸࡾࡶࡥࠨࢄ")] == bstack11111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࠩࢅ"):
                log[bstack11111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬࢆ")] = active[bstack11111_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ࢇ")]
            elif active[bstack11111_opy_ (u"ࠧࡵࡻࡳࡩࠬ࢈")] == bstack11111_opy_ (u"ࠨࡶࡨࡷࡹ࠭ࢉ"):
                log[bstack11111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩࢊ")] = active[bstack11111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪࢋ")]
        bstack1l11lll1_opy_.bstack11llllll_opy_([log])
    def __init__(self):
        self.messages = bstack1l11l1l1_opy_()
        self._1lll1ll1_opy_ = None
        self._1l111lll_opy_ = None
        self._1ll1l1ll_opy_ = OrderedDict()
        self.bstack1ll1l11l_opy_ = bstack1lllll11_opy_(self.bstack1l1lll1l_opy_)
    @error_handler(class_method=True)
    def start_suite(self, name, attrs):
        self.messages.bstack1ll1lll1_opy_()
        if not self._1ll1l1ll_opy_.get(attrs.get(bstack11111_opy_ (u"ࠫ࡮ࡪࠧࢌ")), None):
            self._1ll1l1ll_opy_[attrs.get(bstack11111_opy_ (u"ࠬ࡯ࡤࠨࢍ"))] = {}
        bstack1l11l11l_opy_ = bstack1ll1111l_opy_(
                bstack1ll1l1l1_opy_=attrs.get(bstack11111_opy_ (u"࠭ࡩࡥࠩࢎ")),
                name=name,
                started_at=bstack1l11llll_opy_(),
                file_path=os.path.relpath(attrs[bstack11111_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧ࢏")], start=os.getcwd()) if attrs.get(bstack11111_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨ࢐")) != bstack11111_opy_ (u"ࠩࠪ࢑") else bstack11111_opy_ (u"ࠪࠫ࢒"),
                framework=bstack11111_opy_ (u"ࠫࡗࡵࡢࡰࡶࠪ࢓")
            )
        threading.current_thread().current_suite_id = attrs.get(bstack11111_opy_ (u"ࠬ࡯ࡤࠨ࢔"), None)
        self._1ll1l1ll_opy_[attrs.get(bstack11111_opy_ (u"࠭ࡩࡥࠩ࢕"))][bstack11111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪ࢖")] = bstack1l11l11l_opy_
    @error_handler(class_method=True)
    def end_suite(self, name, attrs):
        messages = self.messages.bstack1ll11l1l_opy_()
        self._1lll1l1l_opy_(messages)
        with self._lock:
            for bstack1lll1l11_opy_ in self.bstack1llll111_opy_:
                bstack1lll1l11_opy_[bstack11111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࠪࢗ")][bstack11111_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨ࢘")].extend(self.store[bstack11111_opy_ (u"ࠪ࡫ࡱࡵࡢࡢ࡮ࡢ࡬ࡴࡵ࡫ࡴ࢙ࠩ")])
                bstack1l11lll1_opy_.bstack1ll11lll_opy_(bstack1lll1l11_opy_)
            self.bstack1llll111_opy_ = []
            self.store[bstack11111_opy_ (u"ࠫ࡬ࡲ࡯ࡣࡣ࡯ࡣ࡭ࡵ࡯࡬ࡵ࢚ࠪ")] = []
    @error_handler(class_method=True)
    def start_test(self, name, attrs):
        self.bstack1ll1l11l_opy_.start()
        if not self._1ll1l1ll_opy_.get(attrs.get(bstack11111_opy_ (u"ࠬ࡯ࡤࠨ࢛")), None):
            self._1ll1l1ll_opy_[attrs.get(bstack11111_opy_ (u"࠭ࡩࡥࠩ࢜"))] = {}
        driver = bstack1l1lllll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭࢝"), None)
        bstack1ll1ll11_opy_ = bstack1ll1111l_opy_(
            bstack1ll1l1l1_opy_=attrs.get(bstack11111_opy_ (u"ࠨ࡫ࡧࠫ࢞")),
            name=name,
            started_at=bstack1l11llll_opy_(),
            file_path=os.path.relpath(attrs[bstack11111_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩ࢟")], start=os.getcwd()),
            scope=RobotHandler.bstack1ll1l111_opy_(attrs.get(bstack11111_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪࢠ"), None)),
            framework=bstack11111_opy_ (u"ࠫࡗࡵࡢࡰࡶࠪࢡ"),
            tags=attrs[bstack11111_opy_ (u"ࠬࡺࡡࡨࡵࠪࢢ")],
            hooks=self.store[bstack11111_opy_ (u"࠭ࡧ࡭ࡱࡥࡥࡱࡥࡨࡰࡱ࡮ࡷࠬࢣ")],
            bstack1lll11ll_opy_=bstack1l11lll1_opy_.bstack1l1l1lll_opy_(driver) if driver and driver.session_id else {},
            meta={},
            code=bstack11111_opy_ (u"ࠢࡼࡿࠣࡠࡳࠦࡻࡾࠤࢤ").format(bstack11111_opy_ (u"ࠣࠢࠥࢥ").join(attrs[bstack11111_opy_ (u"ࠩࡷࡥ࡬ࡹࠧࢦ")]), name) if attrs[bstack11111_opy_ (u"ࠪࡸࡦ࡭ࡳࠨࢧ")] else name
        )
        self._1ll1l1ll_opy_[attrs.get(bstack11111_opy_ (u"ࠫ࡮ࡪࠧࢨ"))][bstack11111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨࢩ")] = bstack1ll1ll11_opy_
        threading.current_thread().current_test_uuid = bstack1ll1ll11_opy_.bstack1llll1l1_opy_()
        threading.current_thread().current_test_id = attrs.get(bstack11111_opy_ (u"࠭ࡩࡥࠩࢪ"), None)
        self.bstack11llll1l_opy_(bstack11111_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨࢫ"), bstack1ll1ll11_opy_)
    @error_handler(class_method=True)
    def end_test(self, name, attrs):
        self.bstack1ll1l11l_opy_.reset()
        bstack1l1llll1_opy_ = bstack11lll1ll_opy_.get(attrs.get(bstack11111_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨࢬ")), bstack11111_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪࢭ"))
        self._1ll1l1ll_opy_[attrs.get(bstack11111_opy_ (u"ࠪ࡭ࡩ࠭ࢮ"))][bstack11111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧࢯ")].stop(time=bstack1l11llll_opy_(), duration=int(attrs.get(bstack11111_opy_ (u"ࠬ࡫࡬ࡢࡲࡶࡩࡩࡺࡩ࡮ࡧࠪࢰ"), bstack11111_opy_ (u"࠭࠰ࠨࢱ"))), result=Result(result=bstack1l1llll1_opy_, exception=attrs.get(bstack11111_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨࢲ")), bstack1l11ll11_opy_=[attrs.get(bstack11111_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩࢳ"))]))
        self.bstack11llll1l_opy_(bstack11111_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫࢴ"), self._1ll1l1ll_opy_[attrs.get(bstack11111_opy_ (u"ࠪ࡭ࡩ࠭ࢵ"))][bstack11111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧࢶ")], True)
        with self._lock:
            self.store[bstack11111_opy_ (u"ࠬࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡴࠩࢷ")] = []
        threading.current_thread().current_test_uuid = None
        threading.current_thread().current_test_id = None
    @error_handler(class_method=True)
    def start_keyword(self, name, attrs):
        self.messages.bstack1ll1lll1_opy_()
        current_test_id = bstack1l1lllll_opy_(threading.current_thread(), bstack11111_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡤࠨࢸ"), None)
        bstack1ll111l1_opy_ = current_test_id if bstack1l1lllll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡥࠩࢹ"), None) else bstack1l1lllll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡶࡹ࡮ࡺࡥࡠ࡫ࡧࠫࢺ"), None)
        if attrs.get(bstack11111_opy_ (u"ࠩࡷࡽࡵ࡫ࠧࢻ"), bstack11111_opy_ (u"ࠪࠫࢼ")).lower() in [bstack11111_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪࢽ"), bstack11111_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴࠧࢾ")]:
            hook_type = bstack1ll111ll_opy_(attrs.get(bstack11111_opy_ (u"࠭ࡴࡺࡲࡨࠫࢿ")), bstack1l1lllll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫࣀ"), None))
            hook_name = bstack11111_opy_ (u"ࠨࡽࢀࠫࣁ").format(attrs.get(bstack11111_opy_ (u"ࠩ࡮ࡻࡳࡧ࡭ࡦࠩࣂ"), bstack11111_opy_ (u"ࠪࠫࣃ")))
            if hook_type in [bstack11111_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡆࡒࡌࠨࣄ"), bstack11111_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡆࡒࡌࠨࣅ")]:
                hook_name = bstack11111_opy_ (u"࡛࠭ࡼࡿࡠࠤࢀࢃࠧࣆ").format(bstack1ll11111_opy_.get(hook_type), attrs.get(bstack11111_opy_ (u"ࠧ࡬ࡹࡱࡥࡲ࡫ࠧࣇ"), bstack11111_opy_ (u"ࠨࠩࣈ")))
            bstack1l111ll1_opy_ = bstack1l11l1ll_opy_(
                bstack1ll1l1l1_opy_=bstack1ll111l1_opy_ + bstack11111_opy_ (u"ࠩ࠰ࠫࣉ") + attrs.get(bstack11111_opy_ (u"ࠪࡸࡾࡶࡥࠨ࣊"), bstack11111_opy_ (u"ࠫࠬ࣋")).lower(),
                name=hook_name,
                started_at=bstack1l11llll_opy_(),
                file_path=os.path.relpath(attrs.get(bstack11111_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬ࣌")), start=os.getcwd()),
                framework=bstack11111_opy_ (u"࠭ࡒࡰࡤࡲࡸࠬ࣍"),
                tags=attrs[bstack11111_opy_ (u"ࠧࡵࡣࡪࡷࠬ࣎")],
                scope=RobotHandler.bstack1ll1l111_opy_(attrs.get(bstack11111_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨ࣏"), None)),
                hook_type=hook_type,
                meta={}
            )
            threading.current_thread().current_hook_uuid = bstack1l111ll1_opy_.bstack1llll1l1_opy_()
            threading.current_thread().current_hook_id = bstack1ll111l1_opy_ + bstack11111_opy_ (u"ࠩ࠰࣐ࠫ") + attrs.get(bstack11111_opy_ (u"ࠪࡸࡾࡶࡥࠨ࣑"), bstack11111_opy_ (u"࣒ࠫࠬ")).lower()
            with self._lock:
                self.store[bstack11111_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥ࣓ࠩ")] = [bstack1l111ll1_opy_.bstack1llll1l1_opy_()]
                if bstack1l1lllll_opy_(threading.current_thread(), bstack11111_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪࣔ"), None):
                    self.store[bstack11111_opy_ (u"ࠧࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡶࠫࣕ")].append(bstack1l111ll1_opy_.bstack1llll1l1_opy_())
                else:
                    self.store[bstack11111_opy_ (u"ࠨࡩ࡯ࡳࡧࡧ࡬ࡠࡪࡲࡳࡰࡹࠧࣖ")].append(bstack1l111ll1_opy_.bstack1llll1l1_opy_())
            if bstack1ll111l1_opy_:
                self._1ll1l1ll_opy_[bstack1ll111l1_opy_ + bstack11111_opy_ (u"ࠩ࠰ࠫࣗ") + attrs.get(bstack11111_opy_ (u"ࠪࡸࡾࡶࡥࠨࣘ"), bstack11111_opy_ (u"ࠫࠬࣙ")).lower()] = { bstack11111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨࣚ"): bstack1l111ll1_opy_ }
            bstack1l11lll1_opy_.bstack11llll1l_opy_(bstack11111_opy_ (u"࠭ࡈࡰࡱ࡮ࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧࣛ"), bstack1l111ll1_opy_)
        else:
            bstack1l1l1l11_opy_ = {
                bstack11111_opy_ (u"ࠧࡪࡦࠪࣜ"): uuid4().__str__(),
                bstack11111_opy_ (u"ࠨࡶࡨࡼࡹ࠭ࣝ"): bstack11111_opy_ (u"ࠩࡾࢁࠥࢁࡽࠨࣞ").format(attrs.get(bstack11111_opy_ (u"ࠪ࡯ࡼࡴࡡ࡮ࡧࠪࣟ")), attrs.get(bstack11111_opy_ (u"ࠫࡦࡸࡧࡴࠩ࣠"), bstack11111_opy_ (u"ࠬ࠭࣡"))) if attrs.get(bstack11111_opy_ (u"࠭ࡡࡳࡩࡶࠫ࣢"), []) else attrs.get(bstack11111_opy_ (u"ࠧ࡬ࡹࡱࡥࡲ࡫ࣣࠧ")),
                bstack11111_opy_ (u"ࠨࡵࡷࡩࡵࡥࡡࡳࡩࡸࡱࡪࡴࡴࠨࣤ"): attrs.get(bstack11111_opy_ (u"ࠩࡤࡶ࡬ࡹࠧࣥ"), []),
                bstack11111_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࣦࠧ"): bstack1l11llll_opy_(),
                bstack11111_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫࣧ"): bstack11111_opy_ (u"ࠬࡶࡥ࡯ࡦ࡬ࡲ࡬࠭ࣨ"),
                bstack11111_opy_ (u"࠭ࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࣩࠫ"): attrs.get(bstack11111_opy_ (u"ࠧࡥࡱࡦࠫ࣪"), bstack11111_opy_ (u"ࠨࠩ࣫"))
            }
            if attrs.get(bstack11111_opy_ (u"ࠩ࡯࡭ࡧࡴࡡ࡮ࡧࠪ࣬"), bstack11111_opy_ (u"࣭ࠪࠫ")) != bstack11111_opy_ (u"࣮ࠫࠬ"):
                bstack1l1l1l11_opy_[bstack11111_opy_ (u"ࠬࡱࡥࡺࡹࡲࡶࡩ࣯࠭")] = attrs.get(bstack11111_opy_ (u"࠭࡬ࡪࡤࡱࡥࡲ࡫ࣰࠧ"))
            if not self.bstack11lllll1_opy_:
                self._1ll1l1ll_opy_[self._1l1l1ll1_opy_()][bstack11111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࣱࠪ")].add_step(bstack1l1l1l11_opy_)
                threading.current_thread().current_step_uuid = bstack1l1l1l11_opy_[bstack11111_opy_ (u"ࠨ࡫ࡧࣲࠫ")]
            self.bstack11lllll1_opy_.append(bstack1l1l1l11_opy_)
    @error_handler(class_method=True)
    def end_keyword(self, name, attrs):
        messages = self.messages.bstack1ll11l1l_opy_()
        self._1lll1l1l_opy_(messages)
        current_test_id = bstack1l1lllll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠ࡫ࡧࠫࣳ"), None)
        bstack1ll111l1_opy_ = current_test_id if current_test_id else bstack1l1lllll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡸࡻࡩࡵࡧࡢ࡭ࡩ࠭ࣴ"), None)
        bstack1l111111_opy_ = bstack11lll1ll_opy_.get(attrs.get(bstack11111_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫࣵ")), bstack11111_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩࣶ࠭"))
        bstack1l11ll1l_opy_ = attrs.get(bstack11111_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧࣷ"))
        if bstack1l111111_opy_ != bstack11111_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨࣸ") and not attrs.get(bstack11111_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࣹࠩ")) and self._1lll1ll1_opy_:
            bstack1l11ll1l_opy_ = self._1lll1ll1_opy_
        bstack1lll1lll_opy_ = Result(result=bstack1l111111_opy_, exception=bstack1l11ll1l_opy_, bstack1l11ll11_opy_=[bstack1l11ll1l_opy_])
        if attrs.get(bstack11111_opy_ (u"ࠩࡷࡽࡵ࡫ࣺࠧ"), bstack11111_opy_ (u"ࠪࠫࣻ")).lower() in [bstack11111_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪࣼ"), bstack11111_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴࠧࣽ")]:
            bstack1ll111l1_opy_ = current_test_id if current_test_id else bstack1l1lllll_opy_(threading.current_thread(), bstack11111_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡴࡷ࡬ࡸࡪࡥࡩࡥࠩࣾ"), None)
            if bstack1ll111l1_opy_:
                bstack1l1ll1l1_opy_ = bstack1ll111l1_opy_ + bstack11111_opy_ (u"ࠢ࠮ࠤࣿ") + attrs.get(bstack11111_opy_ (u"ࠨࡶࡼࡴࡪ࠭ऀ"), bstack11111_opy_ (u"ࠩࠪँ")).lower()
                self._1ll1l1ll_opy_[bstack1l1ll1l1_opy_][bstack11111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭ं")].stop(time=bstack1l11llll_opy_(), duration=int(attrs.get(bstack11111_opy_ (u"ࠫࡪࡲࡡࡱࡵࡨࡨࡹ࡯࡭ࡦࠩः"), bstack11111_opy_ (u"ࠬ࠶ࠧऄ"))), result=bstack1lll1lll_opy_)
                bstack1l11lll1_opy_.bstack11llll1l_opy_(bstack11111_opy_ (u"࠭ࡈࡰࡱ࡮ࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨअ"), self._1ll1l1ll_opy_[bstack1l1ll1l1_opy_][bstack11111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪआ")])
        else:
            bstack1ll111l1_opy_ = current_test_id if current_test_id else bstack1l1lllll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡪࡦࠪइ"), None)
            if bstack1ll111l1_opy_ and len(self.bstack11lllll1_opy_) == 1:
                current_step_uuid = bstack1l1lllll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡷࡹ࡫ࡰࡠࡷࡸ࡭ࡩ࠭ई"), None)
                self._1ll1l1ll_opy_[bstack1ll111l1_opy_][bstack11111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭उ")].bstack1l1l1111_opy_(current_step_uuid, duration=int(attrs.get(bstack11111_opy_ (u"ࠫࡪࡲࡡࡱࡵࡨࡨࡹ࡯࡭ࡦࠩऊ"), bstack11111_opy_ (u"ࠬ࠶ࠧऋ"))), result=bstack1lll1lll_opy_)
            else:
                self.bstack1l1l11ll_opy_(attrs)
            self.bstack11lllll1_opy_.pop()
    def log_message(self, message):
        try:
            if message.get(bstack11111_opy_ (u"࠭ࡨࡵ࡯࡯ࠫऌ"), bstack11111_opy_ (u"ࠧ࡯ࡱࠪऍ")) == bstack11111_opy_ (u"ࠨࡻࡨࡷࠬऎ"):
                return
            self.messages.push(message)
            logs = []
            if bstack11llll11_opy_.bstack11lll1l1_opy_():
                logs.append({
                    bstack11111_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬए"): bstack1l11llll_opy_(),
                    bstack11111_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫऐ"): message.get(bstack11111_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬऑ")),
                    bstack11111_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫऒ"): message.get(bstack11111_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬओ")),
                    **bstack11llll11_opy_.bstack11lll1l1_opy_()
                })
                if len(logs) > 0:
                    bstack1l11lll1_opy_.bstack11llllll_opy_(logs)
        except Exception as err:
            pass
    def close(self):
        bstack1l11lll1_opy_.bstack1l1l1l1l_opy_()
    def bstack1l1l11ll_opy_(self, bstack1llll11l_opy_):
        if not bstack11llll11_opy_.bstack11lll1l1_opy_():
            return
        kwname = bstack11111_opy_ (u"ࠧࡼࡿࠣࡿࢂ࠭औ").format(bstack1llll11l_opy_.get(bstack11111_opy_ (u"ࠨ࡭ࡺࡲࡦࡳࡥࠨक")), bstack1llll11l_opy_.get(bstack11111_opy_ (u"ࠩࡤࡶ࡬ࡹࠧख"), bstack11111_opy_ (u"ࠪࠫग"))) if bstack1llll11l_opy_.get(bstack11111_opy_ (u"ࠫࡦࡸࡧࡴࠩघ"), []) else bstack1llll11l_opy_.get(bstack11111_opy_ (u"ࠬࡱࡷ࡯ࡣࡰࡩࠬङ"))
        error_message = bstack11111_opy_ (u"ࠨ࡫ࡸࡰࡤࡱࡪࡀࠠ࡝ࠤࡾ࠴ࢂࡢࠢࠡࡾࠣࡷࡹࡧࡴࡶࡵ࠽ࠤࡡࠨࡻ࠲ࡿ࡟ࠦࠥࢂࠠࡦࡺࡦࡩࡵࡺࡩࡰࡰ࠽ࠤࡡࠨࡻ࠳ࡿ࡟ࠦࠧच").format(kwname, bstack1llll11l_opy_.get(bstack11111_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧछ")), str(bstack1llll11l_opy_.get(bstack11111_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩज"))))
        bstack1l1l11l1_opy_ = bstack11111_opy_ (u"ࠤ࡮ࡻࡳࡧ࡭ࡦ࠼ࠣࡠࠧࢁ࠰ࡾ࡞ࠥࠤࢁࠦࡳࡵࡣࡷࡹࡸࡀࠠ࡝ࠤࡾ࠵ࢂࡢࠢࠣझ").format(kwname, bstack1llll11l_opy_.get(bstack11111_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪञ")))
        bstack1lll1111_opy_ = error_message if bstack1llll11l_opy_.get(bstack11111_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬट")) else bstack1l1l11l1_opy_
        bstack1lll111l_opy_ = {
            bstack11111_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨठ"): self.bstack11lllll1_opy_[-1].get(bstack11111_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪड"), bstack1l11llll_opy_()),
            bstack11111_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨढ"): bstack1lll1111_opy_,
            bstack11111_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧण"): bstack11111_opy_ (u"ࠩࡈࡖࡗࡕࡒࠨत") if bstack1llll11l_opy_.get(bstack11111_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪथ")) == bstack11111_opy_ (u"ࠫࡋࡇࡉࡍࠩद") else bstack11111_opy_ (u"ࠬࡏࡎࡇࡑࠪध"),
            **bstack11llll11_opy_.bstack11lll1l1_opy_()
        }
        bstack1l11lll1_opy_.bstack11llllll_opy_([bstack1lll111l_opy_])
    def _1l1l1ll1_opy_(self):
        for bstack1ll1l1l1_opy_ in reversed(self._1ll1l1ll_opy_):
            bstack1ll1llll_opy_ = bstack1ll1l1l1_opy_
            data = self._1ll1l1ll_opy_[bstack1ll1l1l1_opy_][bstack11111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩन")]
            if isinstance(data, bstack1l11l1ll_opy_):
                if not bstack11111_opy_ (u"ࠧࡆࡃࡆࡌࠬऩ") in data.bstack1l1ll1ll_opy_():
                    return bstack1ll1llll_opy_
            else:
                return bstack1ll1llll_opy_
    def _1lll1l1l_opy_(self, messages):
        try:
            bstack1lll11l1_opy_ = BuiltIn().get_variable_value(bstack11111_opy_ (u"ࠣࠦࡾࡐࡔࡍࠠࡍࡇ࡙ࡉࡑࢃࠢप")) in (bstack1ll11l11_opy_.DEBUG, bstack1ll11l11_opy_.TRACE)
            for message, bstack1l1ll111_opy_ in zip_longest(messages, messages[1:]):
                name = message.get(bstack11111_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪफ"))
                level = message.get(bstack11111_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩब"))
                if level == bstack1ll11l11_opy_.FAIL:
                    self._1lll1ll1_opy_ = name or self._1lll1ll1_opy_
                    self._1l111lll_opy_ = bstack1l1ll111_opy_.get(bstack11111_opy_ (u"ࠦࡲ࡫ࡳࡴࡣࡪࡩࠧभ")) if bstack1lll11l1_opy_ and bstack1l1ll111_opy_ else self._1l111lll_opy_
        except:
            pass
    @classmethod
    def bstack11llll1l_opy_(self, event: str, bstack1l11l111_opy_: bstack1ll11ll1_opy_, bstack1l1l111l_opy_=False):
        if event == bstack11111_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧम"):
            bstack1l11l111_opy_.set(hooks=self.store[bstack11111_opy_ (u"࠭ࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡵࠪय")])
        if event == bstack11111_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔ࡭࡬ࡴࡵ࡫ࡤࠨर"):
            event = bstack11111_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪऱ")
        if bstack1l1l111l_opy_:
            bstack11lll111_opy_ = {
                bstack11111_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭ल"): event,
                bstack1l11l111_opy_.event_key(): bstack1l11l111_opy_.bstack1l11111l_opy_(event)
            }
            with self._lock:
                self.bstack1llll111_opy_.append(bstack11lll111_opy_)
        else:
            bstack1l11lll1_opy_.bstack11llll1l_opy_(event, bstack1l11l111_opy_)
class bstack1l11l1l1_opy_:
    def __init__(self):
        self._1l111l11_opy_ = []
    def bstack1ll1lll1_opy_(self):
        self._1l111l11_opy_.append([])
    def bstack1ll11l1l_opy_(self):
        return self._1l111l11_opy_.pop() if self._1l111l11_opy_ else list()
    def push(self, message):
        self._1l111l11_opy_[-1].append(message) if self._1l111l11_opy_ else self._1l111l11_opy_.append([message])
class bstack1ll11l11_opy_:
    FAIL = bstack11111_opy_ (u"ࠪࡊࡆࡏࡌࠨळ")
    ERROR = bstack11111_opy_ (u"ࠫࡊࡘࡒࡐࡔࠪऴ")
    WARNING = bstack11111_opy_ (u"ࠬ࡝ࡁࡓࡐࠪव")
    bstack1l111l1l_opy_ = bstack11111_opy_ (u"࠭ࡉࡏࡈࡒࠫश")
    DEBUG = bstack11111_opy_ (u"ࠧࡅࡇࡅ࡙ࡌ࠭ष")
    TRACE = bstack11111_opy_ (u"ࠨࡖࡕࡅࡈࡋࠧस")
    bstack1l1ll11l_opy_ = [FAIL, ERROR]
def bstack1l1111ll_opy_(bstack11lll11l_opy_):
    if not bstack11lll11l_opy_:
        return None
    if bstack11lll11l_opy_.get(bstack11111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬह"), None):
        return getattr(bstack11lll11l_opy_[bstack11111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭ऺ")], bstack11111_opy_ (u"ࠫࡺࡻࡩࡥࠩऻ"), None)
    return bstack11lll11l_opy_.get(bstack11111_opy_ (u"ࠬࡻࡵࡪࡦ़ࠪ"), None)
def bstack1ll111ll_opy_(hook_type, current_test_uuid):
    if hook_type.lower() not in [bstack11111_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬऽ"), bstack11111_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࠩा")]:
        return
    if hook_type.lower() == bstack11111_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧि"):
        if current_test_uuid is None:
            return bstack11111_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡄࡐࡑ࠭ी")
        else:
            return bstack11111_opy_ (u"ࠪࡆࡊࡌࡏࡓࡇࡢࡉࡆࡉࡈࠨु")
    elif hook_type.lower() == bstack11111_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠭ू"):
        if current_test_uuid is None:
            return bstack11111_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡆࡒࡌࠨृ")
        else:
            return bstack11111_opy_ (u"࠭ࡁࡇࡖࡈࡖࡤࡋࡁࡄࡊࠪॄ")