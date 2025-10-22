# coding: UTF-8
import sys
bstack1ll1lll_opy_ = sys.version_info [0] == 2
bstack1l1ll_opy_ = 2048
bstack11l1l1_opy_ = 7
def bstack111l1l_opy_ (bstack1l_opy_):
    global bstack11111ll_opy_
    bstack1lll11l_opy_ = ord (bstack1l_opy_ [-1])
    bstack111ll1_opy_ = bstack1l_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1lll11l_opy_ % len (bstack111ll1_opy_)
    bstack11l111_opy_ = bstack111ll1_opy_ [:bstack1ll11l_opy_] + bstack111ll1_opy_ [bstack1ll11l_opy_:]
    if bstack1ll1lll_opy_:
        bstack1l11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    else:
        bstack1l11l11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    return eval (bstack1l11l11_opy_)
import os
import threading
from uuid import uuid4
from itertools import zip_longest
from collections import OrderedDict
from robot.libraries.BuiltIn import BuiltIn
from browserstack_sdk.bstack11lll11l_opy_ import RobotHandler
from bstack_utils.capture import bstack1l1ll1ll_opy_
from bstack_utils.bstack1l1l11ll_opy_ import bstack11lll1ll_opy_, bstack1l1lllll_opy_, bstack1l1l1ll1_opy_
from bstack_utils.bstack1llll111_opy_ import bstack1lll1111_opy_
from bstack_utils.bstack1l1llll1_opy_ import bstack1l1l1111_opy_
from bstack_utils.constants import *
from bstack_utils.helper import bstack1l11l1ll_opy_, bstack1lllll11_opy_, Result, \
    error_handler, bstack1l1ll111_opy_
class bstack_robot_listener:
    ROBOT_LISTENER_API_VERSION = 2
    _lock = threading.Lock()
    store = {
        bstack111l1l_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧࡶ"): [],
        bstack111l1l_opy_ (u"ࠫ࡬ࡲ࡯ࡣࡣ࡯ࡣ࡭ࡵ࡯࡬ࡵࠪࡷ"): [],
        bstack111l1l_opy_ (u"ࠬࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡴࠩࡸ"): []
    }
    bstack1l1l11l1_opy_ = []
    bstack1l111ll1_opy_ = []
    @staticmethod
    def bstack1ll11l11_opy_(log):
        if not ((isinstance(log[bstack111l1l_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧࡹ")], list) or (isinstance(log[bstack111l1l_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨࡺ")], dict)) and len(log[bstack111l1l_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩࡻ")])>0) or (isinstance(log[bstack111l1l_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪࡼ")], str) and log[bstack111l1l_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫࡽ")].strip())):
            return
        active = bstack1lll1111_opy_.bstack1ll11111_opy_()
        log = {
            bstack111l1l_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪࡾ"): log[bstack111l1l_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫࡿ")],
            bstack111l1l_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩࢀ"): bstack1l1ll111_opy_().isoformat() + bstack111l1l_opy_ (u"࡛ࠧࠩࢁ"),
            bstack111l1l_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩࢂ"): log[bstack111l1l_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪࢃ")],
        }
        if active:
            if active[bstack111l1l_opy_ (u"ࠪࡸࡾࡶࡥࠨࢄ")] == bstack111l1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࠩࢅ"):
                log[bstack111l1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬࢆ")] = active[bstack111l1l_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ࢇ")]
            elif active[bstack111l1l_opy_ (u"ࠧࡵࡻࡳࡩࠬ࢈")] == bstack111l1l_opy_ (u"ࠨࡶࡨࡷࡹ࠭ࢉ"):
                log[bstack111l1l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩࢊ")] = active[bstack111l1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪࢋ")]
        bstack1l1l1111_opy_.bstack1ll1111l_opy_([log])
    def __init__(self):
        self.messages = bstack1l11ll11_opy_()
        self._1l1l1l1l_opy_ = None
        self._1ll11lll_opy_ = None
        self._1ll111ll_opy_ = OrderedDict()
        self.bstack1l11ll1l_opy_ = bstack1l1ll1ll_opy_(self.bstack1ll11l11_opy_)
    @error_handler(class_method=True)
    def start_suite(self, name, attrs):
        self.messages.bstack1l111l1l_opy_()
        if not self._1ll111ll_opy_.get(attrs.get(bstack111l1l_opy_ (u"ࠫ࡮ࡪࠧࢌ")), None):
            self._1ll111ll_opy_[attrs.get(bstack111l1l_opy_ (u"ࠬ࡯ࡤࠨࢍ"))] = {}
        bstack1l1111ll_opy_ = bstack1l1l1ll1_opy_(
                bstack1l1lll1l_opy_=attrs.get(bstack111l1l_opy_ (u"࠭ࡩࡥࠩࢎ")),
                name=name,
                started_at=bstack1lllll11_opy_(),
                file_path=os.path.relpath(attrs[bstack111l1l_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧ࢏")], start=os.getcwd()) if attrs.get(bstack111l1l_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨ࢐")) != bstack111l1l_opy_ (u"ࠩࠪ࢑") else bstack111l1l_opy_ (u"ࠪࠫ࢒"),
                framework=bstack111l1l_opy_ (u"ࠫࡗࡵࡢࡰࡶࠪ࢓")
            )
        threading.current_thread().current_suite_id = attrs.get(bstack111l1l_opy_ (u"ࠬ࡯ࡤࠨ࢔"), None)
        self._1ll111ll_opy_[attrs.get(bstack111l1l_opy_ (u"࠭ࡩࡥࠩ࢕"))][bstack111l1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪ࢖")] = bstack1l1111ll_opy_
    @error_handler(class_method=True)
    def end_suite(self, name, attrs):
        messages = self.messages.bstack1l1l1l11_opy_()
        self._11lllll1_opy_(messages)
        with self._lock:
            for bstack11llllll_opy_ in self.bstack1l1l11l1_opy_:
                bstack11llllll_opy_[bstack111l1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࠪࢗ")][bstack111l1l_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨ࢘")].extend(self.store[bstack111l1l_opy_ (u"ࠪ࡫ࡱࡵࡢࡢ࡮ࡢ࡬ࡴࡵ࡫ࡴ࢙ࠩ")])
                bstack1l1l1111_opy_.bstack1lll1l1l_opy_(bstack11llllll_opy_)
            self.bstack1l1l11l1_opy_ = []
            self.store[bstack111l1l_opy_ (u"ࠫ࡬ࡲ࡯ࡣࡣ࡯ࡣ࡭ࡵ࡯࡬ࡵ࢚ࠪ")] = []
    @error_handler(class_method=True)
    def start_test(self, name, attrs):
        self.bstack1l11ll1l_opy_.start()
        if not self._1ll111ll_opy_.get(attrs.get(bstack111l1l_opy_ (u"ࠬ࡯ࡤࠨ࢛")), None):
            self._1ll111ll_opy_[attrs.get(bstack111l1l_opy_ (u"࠭ࡩࡥࠩ࢜"))] = {}
        driver = bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭࢝"), None)
        bstack1l1l11ll_opy_ = bstack1l1l1ll1_opy_(
            bstack1l1lll1l_opy_=attrs.get(bstack111l1l_opy_ (u"ࠨ࡫ࡧࠫ࢞")),
            name=name,
            started_at=bstack1lllll11_opy_(),
            file_path=os.path.relpath(attrs[bstack111l1l_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩ࢟")], start=os.getcwd()),
            scope=RobotHandler.bstack1l11l11l_opy_(attrs.get(bstack111l1l_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪࢠ"), None)),
            framework=bstack111l1l_opy_ (u"ࠫࡗࡵࡢࡰࡶࠪࢡ"),
            tags=attrs[bstack111l1l_opy_ (u"ࠬࡺࡡࡨࡵࠪࢢ")],
            hooks=self.store[bstack111l1l_opy_ (u"࠭ࡧ࡭ࡱࡥࡥࡱࡥࡨࡰࡱ࡮ࡷࠬࢣ")],
            bstack1llll11l_opy_=bstack1l1l1111_opy_.bstack1ll1l1ll_opy_(driver) if driver and driver.session_id else {},
            meta={},
            code=bstack111l1l_opy_ (u"ࠢࡼࡿࠣࡠࡳࠦࡻࡾࠤࢤ").format(bstack111l1l_opy_ (u"ࠣࠢࠥࢥ").join(attrs[bstack111l1l_opy_ (u"ࠩࡷࡥ࡬ࡹࠧࢦ")]), name) if attrs[bstack111l1l_opy_ (u"ࠪࡸࡦ࡭ࡳࠨࢧ")] else name
        )
        self._1ll111ll_opy_[attrs.get(bstack111l1l_opy_ (u"ࠫ࡮ࡪࠧࢨ"))][bstack111l1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨࢩ")] = bstack1l1l11ll_opy_
        threading.current_thread().current_test_uuid = bstack1l1l11ll_opy_.bstack1lll1l11_opy_()
        threading.current_thread().current_test_id = attrs.get(bstack111l1l_opy_ (u"࠭ࡩࡥࠩࢪ"), None)
        self.bstack1l1l111l_opy_(bstack111l1l_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨࢫ"), bstack1l1l11ll_opy_)
    @error_handler(class_method=True)
    def end_test(self, name, attrs):
        self.bstack1l11ll1l_opy_.reset()
        bstack1llll1ll_opy_ = bstack1l111111_opy_.get(attrs.get(bstack111l1l_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨࢬ")), bstack111l1l_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪࢭ"))
        self._1ll111ll_opy_[attrs.get(bstack111l1l_opy_ (u"ࠪ࡭ࡩ࠭ࢮ"))][bstack111l1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧࢯ")].stop(time=bstack1lllll11_opy_(), duration=int(attrs.get(bstack111l1l_opy_ (u"ࠬ࡫࡬ࡢࡲࡶࡩࡩࡺࡩ࡮ࡧࠪࢰ"), bstack111l1l_opy_ (u"࠭࠰ࠨࢱ"))), result=Result(result=bstack1llll1ll_opy_, exception=attrs.get(bstack111l1l_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨࢲ")), bstack11lll111_opy_=[attrs.get(bstack111l1l_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩࢳ"))]))
        self.bstack1l1l111l_opy_(bstack111l1l_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫࢴ"), self._1ll111ll_opy_[attrs.get(bstack111l1l_opy_ (u"ࠪ࡭ࡩ࠭ࢵ"))][bstack111l1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧࢶ")], True)
        with self._lock:
            self.store[bstack111l1l_opy_ (u"ࠬࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡴࠩࢷ")] = []
        threading.current_thread().current_test_uuid = None
        threading.current_thread().current_test_id = None
    @error_handler(class_method=True)
    def start_keyword(self, name, attrs):
        self.messages.bstack1l111l1l_opy_()
        current_test_id = bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡤࠨࢸ"), None)
        bstack1ll11ll1_opy_ = current_test_id if bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡥࠩࢹ"), None) else bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡶࡹ࡮ࡺࡥࡠ࡫ࡧࠫࢺ"), None)
        if attrs.get(bstack111l1l_opy_ (u"ࠩࡷࡽࡵ࡫ࠧࢻ"), bstack111l1l_opy_ (u"ࠪࠫࢼ")).lower() in [bstack111l1l_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪࢽ"), bstack111l1l_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴࠧࢾ")]:
            hook_type = bstack1lll11ll_opy_(attrs.get(bstack111l1l_opy_ (u"࠭ࡴࡺࡲࡨࠫࢿ")), bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫࣀ"), None))
            hook_name = bstack111l1l_opy_ (u"ࠨࡽࢀࠫࣁ").format(attrs.get(bstack111l1l_opy_ (u"ࠩ࡮ࡻࡳࡧ࡭ࡦࠩࣂ"), bstack111l1l_opy_ (u"ࠪࠫࣃ")))
            if hook_type in [bstack111l1l_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡆࡒࡌࠨࣄ"), bstack111l1l_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡆࡒࡌࠨࣅ")]:
                hook_name = bstack111l1l_opy_ (u"࡛࠭ࡼࡿࡠࠤࢀࢃࠧࣆ").format(bstack1l11llll_opy_.get(hook_type), attrs.get(bstack111l1l_opy_ (u"ࠧ࡬ࡹࡱࡥࡲ࡫ࠧࣇ"), bstack111l1l_opy_ (u"ࠨࠩࣈ")))
            bstack1llll1l1_opy_ = bstack1l1lllll_opy_(
                bstack1l1lll1l_opy_=bstack1ll11ll1_opy_ + bstack111l1l_opy_ (u"ࠩ࠰ࠫࣉ") + attrs.get(bstack111l1l_opy_ (u"ࠪࡸࡾࡶࡥࠨ࣊"), bstack111l1l_opy_ (u"ࠫࠬ࣋")).lower(),
                name=hook_name,
                started_at=bstack1lllll11_opy_(),
                file_path=os.path.relpath(attrs.get(bstack111l1l_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬ࣌")), start=os.getcwd()),
                framework=bstack111l1l_opy_ (u"࠭ࡒࡰࡤࡲࡸࠬ࣍"),
                tags=attrs[bstack111l1l_opy_ (u"ࠧࡵࡣࡪࡷࠬ࣎")],
                scope=RobotHandler.bstack1l11l11l_opy_(attrs.get(bstack111l1l_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨ࣏"), None)),
                hook_type=hook_type,
                meta={}
            )
            threading.current_thread().current_hook_uuid = bstack1llll1l1_opy_.bstack1lll1l11_opy_()
            threading.current_thread().current_hook_id = bstack1ll11ll1_opy_ + bstack111l1l_opy_ (u"ࠩ࠰࣐ࠫ") + attrs.get(bstack111l1l_opy_ (u"ࠪࡸࡾࡶࡥࠨ࣑"), bstack111l1l_opy_ (u"࣒ࠫࠬ")).lower()
            with self._lock:
                self.store[bstack111l1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥ࣓ࠩ")] = [bstack1llll1l1_opy_.bstack1lll1l11_opy_()]
                if bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪࣔ"), None):
                    self.store[bstack111l1l_opy_ (u"ࠧࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡶࠫࣕ")].append(bstack1llll1l1_opy_.bstack1lll1l11_opy_())
                else:
                    self.store[bstack111l1l_opy_ (u"ࠨࡩ࡯ࡳࡧࡧ࡬ࡠࡪࡲࡳࡰࡹࠧࣖ")].append(bstack1llll1l1_opy_.bstack1lll1l11_opy_())
            if bstack1ll11ll1_opy_:
                self._1ll111ll_opy_[bstack1ll11ll1_opy_ + bstack111l1l_opy_ (u"ࠩ࠰ࠫࣗ") + attrs.get(bstack111l1l_opy_ (u"ࠪࡸࡾࡶࡥࠨࣘ"), bstack111l1l_opy_ (u"ࠫࠬࣙ")).lower()] = { bstack111l1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨࣚ"): bstack1llll1l1_opy_ }
            bstack1l1l1111_opy_.bstack1l1l111l_opy_(bstack111l1l_opy_ (u"࠭ࡈࡰࡱ࡮ࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧࣛ"), bstack1llll1l1_opy_)
        else:
            bstack1lll11l1_opy_ = {
                bstack111l1l_opy_ (u"ࠧࡪࡦࠪࣜ"): uuid4().__str__(),
                bstack111l1l_opy_ (u"ࠨࡶࡨࡼࡹ࠭ࣝ"): bstack111l1l_opy_ (u"ࠩࡾࢁࠥࢁࡽࠨࣞ").format(attrs.get(bstack111l1l_opy_ (u"ࠪ࡯ࡼࡴࡡ࡮ࡧࠪࣟ")), attrs.get(bstack111l1l_opy_ (u"ࠫࡦࡸࡧࡴࠩ࣠"), bstack111l1l_opy_ (u"ࠬ࠭࣡"))) if attrs.get(bstack111l1l_opy_ (u"࠭ࡡࡳࡩࡶࠫ࣢"), []) else attrs.get(bstack111l1l_opy_ (u"ࠧ࡬ࡹࡱࡥࡲ࡫ࣣࠧ")),
                bstack111l1l_opy_ (u"ࠨࡵࡷࡩࡵࡥࡡࡳࡩࡸࡱࡪࡴࡴࠨࣤ"): attrs.get(bstack111l1l_opy_ (u"ࠩࡤࡶ࡬ࡹࠧࣥ"), []),
                bstack111l1l_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࣦࠧ"): bstack1lllll11_opy_(),
                bstack111l1l_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫࣧ"): bstack111l1l_opy_ (u"ࠬࡶࡥ࡯ࡦ࡬ࡲ࡬࠭ࣨ"),
                bstack111l1l_opy_ (u"࠭ࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࣩࠫ"): attrs.get(bstack111l1l_opy_ (u"ࠧࡥࡱࡦࠫ࣪"), bstack111l1l_opy_ (u"ࠨࠩ࣫"))
            }
            if attrs.get(bstack111l1l_opy_ (u"ࠩ࡯࡭ࡧࡴࡡ࡮ࡧࠪ࣬"), bstack111l1l_opy_ (u"࣭ࠪࠫ")) != bstack111l1l_opy_ (u"࣮ࠫࠬ"):
                bstack1lll11l1_opy_[bstack111l1l_opy_ (u"ࠬࡱࡥࡺࡹࡲࡶࡩ࣯࠭")] = attrs.get(bstack111l1l_opy_ (u"࠭࡬ࡪࡤࡱࡥࡲ࡫ࣰࠧ"))
            if not self.bstack1l111ll1_opy_:
                self._1ll111ll_opy_[self._1lll111l_opy_()][bstack111l1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࣱࠪ")].add_step(bstack1lll11l1_opy_)
                threading.current_thread().current_step_uuid = bstack1lll11l1_opy_[bstack111l1l_opy_ (u"ࠨ࡫ࡧࣲࠫ")]
            self.bstack1l111ll1_opy_.append(bstack1lll11l1_opy_)
    @error_handler(class_method=True)
    def end_keyword(self, name, attrs):
        messages = self.messages.bstack1l1l1l11_opy_()
        self._11lllll1_opy_(messages)
        current_test_id = bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠ࡫ࡧࠫࣳ"), None)
        bstack1ll11ll1_opy_ = current_test_id if current_test_id else bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡸࡻࡩࡵࡧࡢ࡭ࡩ࠭ࣴ"), None)
        bstack1l111l11_opy_ = bstack1l111111_opy_.get(attrs.get(bstack111l1l_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫࣵ")), bstack111l1l_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩࣶ࠭"))
        bstack1l1111l1_opy_ = attrs.get(bstack111l1l_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧࣷ"))
        if bstack1l111l11_opy_ != bstack111l1l_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨࣸ") and not attrs.get(bstack111l1l_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࣹࠩ")) and self._1l1l1l1l_opy_:
            bstack1l1111l1_opy_ = self._1l1l1l1l_opy_
        bstack1ll11l1l_opy_ = Result(result=bstack1l111l11_opy_, exception=bstack1l1111l1_opy_, bstack11lll111_opy_=[bstack1l1111l1_opy_])
        if attrs.get(bstack111l1l_opy_ (u"ࠩࡷࡽࡵ࡫ࣺࠧ"), bstack111l1l_opy_ (u"ࠪࠫࣻ")).lower() in [bstack111l1l_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪࣼ"), bstack111l1l_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴࠧࣽ")]:
            bstack1ll11ll1_opy_ = current_test_id if current_test_id else bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡴࡷ࡬ࡸࡪࡥࡩࡥࠩࣾ"), None)
            if bstack1ll11ll1_opy_:
                bstack1l11l1l1_opy_ = bstack1ll11ll1_opy_ + bstack111l1l_opy_ (u"ࠢ࠮ࠤࣿ") + attrs.get(bstack111l1l_opy_ (u"ࠨࡶࡼࡴࡪ࠭ऀ"), bstack111l1l_opy_ (u"ࠩࠪँ")).lower()
                self._1ll111ll_opy_[bstack1l11l1l1_opy_][bstack111l1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭ं")].stop(time=bstack1lllll11_opy_(), duration=int(attrs.get(bstack111l1l_opy_ (u"ࠫࡪࡲࡡࡱࡵࡨࡨࡹ࡯࡭ࡦࠩः"), bstack111l1l_opy_ (u"ࠬ࠶ࠧऄ"))), result=bstack1ll11l1l_opy_)
                bstack1l1l1111_opy_.bstack1l1l111l_opy_(bstack111l1l_opy_ (u"࠭ࡈࡰࡱ࡮ࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨअ"), self._1ll111ll_opy_[bstack1l11l1l1_opy_][bstack111l1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪआ")])
        else:
            bstack1ll11ll1_opy_ = current_test_id if current_test_id else bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡪࡦࠪइ"), None)
            if bstack1ll11ll1_opy_ and len(self.bstack1l111ll1_opy_) == 1:
                current_step_uuid = bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡷࡹ࡫ࡰࡠࡷࡸ࡭ࡩ࠭ई"), None)
                self._1ll111ll_opy_[bstack1ll11ll1_opy_][bstack111l1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭उ")].bstack1lll1lll_opy_(current_step_uuid, duration=int(attrs.get(bstack111l1l_opy_ (u"ࠫࡪࡲࡡࡱࡵࡨࡨࡹ࡯࡭ࡦࠩऊ"), bstack111l1l_opy_ (u"ࠬ࠶ࠧऋ"))), result=bstack1ll11l1l_opy_)
            else:
                self.bstack1ll1ll1l_opy_(attrs)
            self.bstack1l111ll1_opy_.pop()
    def log_message(self, message):
        try:
            if message.get(bstack111l1l_opy_ (u"࠭ࡨࡵ࡯࡯ࠫऌ"), bstack111l1l_opy_ (u"ࠧ࡯ࡱࠪऍ")) == bstack111l1l_opy_ (u"ࠨࡻࡨࡷࠬऎ"):
                return
            self.messages.push(message)
            logs = []
            if bstack1lll1111_opy_.bstack1ll11111_opy_():
                logs.append({
                    bstack111l1l_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬए"): bstack1lllll11_opy_(),
                    bstack111l1l_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫऐ"): message.get(bstack111l1l_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬऑ")),
                    bstack111l1l_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫऒ"): message.get(bstack111l1l_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬओ")),
                    **bstack1lll1111_opy_.bstack1ll11111_opy_()
                })
                if len(logs) > 0:
                    bstack1l1l1111_opy_.bstack1ll1111l_opy_(logs)
        except Exception as err:
            pass
    def close(self):
        bstack1l1l1111_opy_.bstack1l1l1lll_opy_()
    def bstack1ll1ll1l_opy_(self, bstack1lll1ll1_opy_):
        if not bstack1lll1111_opy_.bstack1ll11111_opy_():
            return
        kwname = bstack111l1l_opy_ (u"ࠧࡼࡿࠣࡿࢂ࠭औ").format(bstack1lll1ll1_opy_.get(bstack111l1l_opy_ (u"ࠨ࡭ࡺࡲࡦࡳࡥࠨक")), bstack1lll1ll1_opy_.get(bstack111l1l_opy_ (u"ࠩࡤࡶ࡬ࡹࠧख"), bstack111l1l_opy_ (u"ࠪࠫग"))) if bstack1lll1ll1_opy_.get(bstack111l1l_opy_ (u"ࠫࡦࡸࡧࡴࠩघ"), []) else bstack1lll1ll1_opy_.get(bstack111l1l_opy_ (u"ࠬࡱࡷ࡯ࡣࡰࡩࠬङ"))
        error_message = bstack111l1l_opy_ (u"ࠨ࡫ࡸࡰࡤࡱࡪࡀࠠ࡝ࠤࡾ࠴ࢂࡢࠢࠡࡾࠣࡷࡹࡧࡴࡶࡵ࠽ࠤࡡࠨࡻ࠲ࡿ࡟ࠦࠥࢂࠠࡦࡺࡦࡩࡵࡺࡩࡰࡰ࠽ࠤࡡࠨࡻ࠳ࡿ࡟ࠦࠧच").format(kwname, bstack1lll1ll1_opy_.get(bstack111l1l_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧछ")), str(bstack1lll1ll1_opy_.get(bstack111l1l_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩज"))))
        bstack1l11lll1_opy_ = bstack111l1l_opy_ (u"ࠤ࡮ࡻࡳࡧ࡭ࡦ࠼ࠣࡠࠧࢁ࠰ࡾ࡞ࠥࠤࢁࠦࡳࡵࡣࡷࡹࡸࡀࠠ࡝ࠤࡾ࠵ࢂࡢࠢࠣझ").format(kwname, bstack1lll1ll1_opy_.get(bstack111l1l_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪञ")))
        bstack1ll1l1l1_opy_ = error_message if bstack1lll1ll1_opy_.get(bstack111l1l_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬट")) else bstack1l11lll1_opy_
        bstack1l1ll11l_opy_ = {
            bstack111l1l_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨठ"): self.bstack1l111ll1_opy_[-1].get(bstack111l1l_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪड"), bstack1lllll11_opy_()),
            bstack111l1l_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨढ"): bstack1ll1l1l1_opy_,
            bstack111l1l_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧण"): bstack111l1l_opy_ (u"ࠩࡈࡖࡗࡕࡒࠨत") if bstack1lll1ll1_opy_.get(bstack111l1l_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪथ")) == bstack111l1l_opy_ (u"ࠫࡋࡇࡉࡍࠩद") else bstack111l1l_opy_ (u"ࠬࡏࡎࡇࡑࠪध"),
            **bstack1lll1111_opy_.bstack1ll11111_opy_()
        }
        bstack1l1l1111_opy_.bstack1ll1111l_opy_([bstack1l1ll11l_opy_])
    def _1lll111l_opy_(self):
        for bstack1l1lll1l_opy_ in reversed(self._1ll111ll_opy_):
            bstack1l11l111_opy_ = bstack1l1lll1l_opy_
            data = self._1ll111ll_opy_[bstack1l1lll1l_opy_][bstack111l1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩन")]
            if isinstance(data, bstack1l1lllll_opy_):
                if not bstack111l1l_opy_ (u"ࠧࡆࡃࡆࡌࠬऩ") in data.bstack11llll1l_opy_():
                    return bstack1l11l111_opy_
            else:
                return bstack1l11l111_opy_
    def _11lllll1_opy_(self, messages):
        try:
            bstack1ll1llll_opy_ = BuiltIn().get_variable_value(bstack111l1l_opy_ (u"ࠣࠦࡾࡐࡔࡍࠠࡍࡇ࡙ࡉࡑࢃࠢप")) in (bstack1ll1lll1_opy_.DEBUG, bstack1ll1lll1_opy_.TRACE)
            for message, bstack1ll1ll11_opy_ in zip_longest(messages, messages[1:]):
                name = message.get(bstack111l1l_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪफ"))
                level = message.get(bstack111l1l_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩब"))
                if level == bstack1ll1lll1_opy_.FAIL:
                    self._1l1l1l1l_opy_ = name or self._1l1l1l1l_opy_
                    self._1ll11lll_opy_ = bstack1ll1ll11_opy_.get(bstack111l1l_opy_ (u"ࠦࡲ࡫ࡳࡴࡣࡪࡩࠧभ")) if bstack1ll1llll_opy_ and bstack1ll1ll11_opy_ else self._1ll11lll_opy_
        except:
            pass
    @classmethod
    def bstack1l1l111l_opy_(self, event: str, bstack1l1ll1l1_opy_: bstack11lll1ll_opy_, bstack1l11111l_opy_=False):
        if event == bstack111l1l_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧम"):
            bstack1l1ll1l1_opy_.set(hooks=self.store[bstack111l1l_opy_ (u"࠭ࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡵࠪय")])
        if event == bstack111l1l_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔ࡭࡬ࡴࡵ࡫ࡤࠨर"):
            event = bstack111l1l_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪऱ")
        if bstack1l11111l_opy_:
            bstack1l111lll_opy_ = {
                bstack111l1l_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭ल"): event,
                bstack1l1ll1l1_opy_.event_key(): bstack1l1ll1l1_opy_.bstack11llll11_opy_(event)
            }
            with self._lock:
                self.bstack1l1l11l1_opy_.append(bstack1l111lll_opy_)
        else:
            bstack1l1l1111_opy_.bstack1l1l111l_opy_(event, bstack1l1ll1l1_opy_)
class bstack1l11ll11_opy_:
    def __init__(self):
        self._1ll111l1_opy_ = []
    def bstack1l111l1l_opy_(self):
        self._1ll111l1_opy_.append([])
    def bstack1l1l1l11_opy_(self):
        return self._1ll111l1_opy_.pop() if self._1ll111l1_opy_ else list()
    def push(self, message):
        self._1ll111l1_opy_[-1].append(message) if self._1ll111l1_opy_ else self._1ll111l1_opy_.append([message])
class bstack1ll1lll1_opy_:
    FAIL = bstack111l1l_opy_ (u"ࠪࡊࡆࡏࡌࠨळ")
    ERROR = bstack111l1l_opy_ (u"ࠫࡊࡘࡒࡐࡔࠪऴ")
    WARNING = bstack111l1l_opy_ (u"ࠬ࡝ࡁࡓࡐࠪव")
    bstack1l1lll11_opy_ = bstack111l1l_opy_ (u"࠭ࡉࡏࡈࡒࠫश")
    DEBUG = bstack111l1l_opy_ (u"ࠧࡅࡇࡅ࡙ࡌ࠭ष")
    TRACE = bstack111l1l_opy_ (u"ࠨࡖࡕࡅࡈࡋࠧस")
    bstack1ll1l111_opy_ = [FAIL, ERROR]
def bstack11lll1l1_opy_(bstack1ll1l11l_opy_):
    if not bstack1ll1l11l_opy_:
        return None
    if bstack1ll1l11l_opy_.get(bstack111l1l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬह"), None):
        return getattr(bstack1ll1l11l_opy_[bstack111l1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭ऺ")], bstack111l1l_opy_ (u"ࠫࡺࡻࡩࡥࠩऻ"), None)
    return bstack1ll1l11l_opy_.get(bstack111l1l_opy_ (u"ࠬࡻࡵࡪࡦ़ࠪ"), None)
def bstack1lll11ll_opy_(hook_type, current_test_uuid):
    if hook_type.lower() not in [bstack111l1l_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬऽ"), bstack111l1l_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࠩा")]:
        return
    if hook_type.lower() == bstack111l1l_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧि"):
        if current_test_uuid is None:
            return bstack111l1l_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡄࡐࡑ࠭ी")
        else:
            return bstack111l1l_opy_ (u"ࠪࡆࡊࡌࡏࡓࡇࡢࡉࡆࡉࡈࠨु")
    elif hook_type.lower() == bstack111l1l_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠭ू"):
        if current_test_uuid is None:
            return bstack111l1l_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡆࡒࡌࠨृ")
        else:
            return bstack111l1l_opy_ (u"࠭ࡁࡇࡖࡈࡖࡤࡋࡁࡄࡊࠪॄ")