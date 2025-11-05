# coding: UTF-8
import sys
bstack11_opy_ = sys.version_info [0] == 2
bstack1l111ll_opy_ = 2048
bstack11lll1l_opy_ = 7
def bstack1lll11l_opy_ (bstack11l11l_opy_):
    global bstack11l1l1_opy_
    bstack1l111_opy_ = ord (bstack11l11l_opy_ [-1])
    bstack1ll11l1_opy_ = bstack11l11l_opy_ [:-1]
    bstack1l_opy_ = bstack1l111_opy_ % len (bstack1ll11l1_opy_)
    bstack1l11ll1_opy_ = bstack1ll11l1_opy_ [:bstack1l_opy_] + bstack1ll11l1_opy_ [bstack1l_opy_:]
    if bstack11_opy_:
        bstack1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    else:
        bstack1ll_opy_ = str () .join ([chr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    return eval (bstack1ll_opy_)
import threading
import os
import logging
from uuid import uuid4
from bstack_utils.bstack1l1ll111_opy_ import bstack1l111111_opy_, bstack11llllll_opy_
from bstack_utils.bstack1l1l111l_opy_ import bstack1l11111l_opy_
from bstack_utils.helper import bstack1ll111ll_opy_, bstack1l111lll_opy_, Result
from bstack_utils.bstack1l11lll1_opy_ import bstack1l111l1l_opy_
from bstack_utils.capture import bstack1lll1ll1_opy_
from bstack_utils.constants import *
logger = logging.getLogger(__name__)
class bstack11l1l111_opy_:
    def __init__(self):
        self.bstack1l111l11_opy_ = bstack1lll1ll1_opy_(self.bstack1l11ll11_opy_)
        self.tests = {}
    @staticmethod
    def bstack1l11ll11_opy_(log):
        if not (log[bstack1lll11l_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨॡ")] and log[bstack1lll11l_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩॢ")].strip()):
            return
        active = bstack1l11111l_opy_.bstack1llll11l_opy_()
        log = {
            bstack1lll11l_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨॣ"): log[bstack1lll11l_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩ।")],
            bstack1lll11l_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧ॥"): bstack1l111lll_opy_(),
            bstack1lll11l_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭०"): log[bstack1lll11l_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ१")],
        }
        if active:
            if active[bstack1lll11l_opy_ (u"ࠧࡵࡻࡳࡩࠬ२")] == bstack1lll11l_opy_ (u"ࠨࡪࡲࡳࡰ࠭३"):
                log[bstack1lll11l_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ४")] = active[bstack1lll11l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ५")]
            elif active[bstack1lll11l_opy_ (u"ࠫࡹࡿࡰࡦࠩ६")] == bstack1lll11l_opy_ (u"ࠬࡺࡥࡴࡶࠪ७"):
                log[bstack1lll11l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭८")] = active[bstack1lll11l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ९")]
        bstack1l111l1l_opy_.bstack1l11llll_opy_([log])
    def start_test(self, attrs):
        test_uuid = uuid4().__str__()
        self.tests[test_uuid] = {}
        self.bstack1l111l11_opy_.start()
        driver = bstack1ll111ll_opy_(threading.current_thread(), bstack1lll11l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧ॰"), None)
        bstack1l1ll111_opy_ = bstack11llllll_opy_(
            name=attrs.scenario.name,
            uuid=test_uuid,
            started_at=bstack1l111lll_opy_(),
            file_path=attrs.feature.filename,
            result=bstack1lll11l_opy_ (u"ࠤࡳࡩࡳࡪࡩ࡯ࡩࠥॱ"),
            framework=bstack1lll11l_opy_ (u"ࠪࡆࡪ࡮ࡡࡷࡧࠪॲ"),
            scope=[attrs.feature.name],
            bstack1l1l11l1_opy_=bstack1l111l1l_opy_.bstack1ll1l111_opy_(driver) if driver and driver.session_id else {},
            meta={},
            tags=attrs.scenario.tags
        )
        self.tests[test_uuid][bstack1lll11l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧॳ")] = bstack1l1ll111_opy_
        threading.current_thread().current_test_uuid = test_uuid
        bstack1l111l1l_opy_.bstack1lll1111_opy_(bstack1lll11l_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭ॴ"), bstack1l1ll111_opy_)
    def end_test(self, attrs):
        bstack11l1ll11_opy_ = {
            bstack1lll11l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦॵ"): attrs.feature.name,
            bstack1lll11l_opy_ (u"ࠢࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠧॶ"): attrs.feature.description
        }
        current_test_uuid = threading.current_thread().current_test_uuid
        bstack1l1ll111_opy_ = self.tests[current_test_uuid][bstack1lll11l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫॷ")]
        meta = {
            bstack1lll11l_opy_ (u"ࠤࡩࡩࡦࡺࡵࡳࡧࠥॸ"): bstack11l1ll11_opy_,
            bstack1lll11l_opy_ (u"ࠥࡷࡹ࡫ࡰࡴࠤॹ"): bstack1l1ll111_opy_.meta.get(bstack1lll11l_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪॺ"), []),
            bstack1lll11l_opy_ (u"ࠧࡹࡣࡦࡰࡤࡶ࡮ࡵࠢॻ"): {
                bstack1lll11l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦॼ"): attrs.feature.scenarios[0].name if len(attrs.feature.scenarios) else None
            }
        }
        bstack1l1ll111_opy_.bstack11l1l11l_opy_(meta)
        bstack1l1ll111_opy_.bstack11l11lll_opy_(bstack1ll111ll_opy_(threading.current_thread(), bstack1lll11l_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡷࠬॽ"), []))
        bstack11l11ll1_opy_, exception = self._11l1llll_opy_(attrs)
        bstack1llll111_opy_ = Result(result=attrs.status.name, exception=exception, bstack11lll11l_opy_=[bstack11l11ll1_opy_])
        self.tests[threading.current_thread().current_test_uuid][bstack1lll11l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫॾ")].stop(time=bstack1l111lll_opy_(), duration=int(attrs.duration)*1000, result=bstack1llll111_opy_)
        bstack1l111l1l_opy_.bstack1lll1111_opy_(bstack1lll11l_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫॿ"), self.tests[threading.current_thread().current_test_uuid][bstack1lll11l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭ঀ")])
    def bstack11l1l1ll_opy_(self, attrs):
        bstack1lll11l1_opy_ = {
            bstack1lll11l_opy_ (u"ࠫ࡮ࡪࠧঁ"): uuid4().__str__(),
            bstack1lll11l_opy_ (u"ࠬࡱࡥࡺࡹࡲࡶࡩ࠭ং"): attrs.keyword,
            bstack1lll11l_opy_ (u"࠭ࡳࡵࡧࡳࡣࡦࡸࡧࡶ࡯ࡨࡲࡹ࠭ঃ"): [],
            bstack1lll11l_opy_ (u"ࠧࡵࡧࡻࡸࠬ঄"): attrs.name,
            bstack1lll11l_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬঅ"): bstack1l111lll_opy_(),
            bstack1lll11l_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩআ"): bstack1lll11l_opy_ (u"ࠪࡴࡪࡴࡤࡪࡰࡪࠫই"),
            bstack1lll11l_opy_ (u"ࠫࡩ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠩঈ"): bstack1lll11l_opy_ (u"ࠬ࠭উ")
        }
        self.tests[threading.current_thread().current_test_uuid][bstack1lll11l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩঊ")].add_step(bstack1lll11l1_opy_)
        threading.current_thread().current_step_uuid = bstack1lll11l1_opy_[bstack1lll11l_opy_ (u"ࠧࡪࡦࠪঋ")]
    def bstack11l11l1l_opy_(self, attrs):
        current_test_id = bstack1ll111ll_opy_(threading.current_thread(), bstack1lll11l_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬঌ"), None)
        current_step_uuid = bstack1ll111ll_opy_(threading.current_thread(), bstack1lll11l_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡷࡹ࡫ࡰࡠࡷࡸ࡭ࡩ࠭঍"), None)
        bstack11l11ll1_opy_, exception = self._11l1llll_opy_(attrs)
        bstack1llll111_opy_ = Result(result=attrs.status.name, exception=exception, bstack11lll11l_opy_=[bstack11l11ll1_opy_])
        self.tests[current_test_id][bstack1lll11l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭঎")].bstack1l1l1ll1_opy_(current_step_uuid, duration=int(attrs.duration)*1000, result=bstack1llll111_opy_)
        threading.current_thread().current_step_uuid = None
    def bstack11l1lll1_opy_(self, name, attrs):
        try:
            bstack11l1ll1l_opy_ = uuid4().__str__()
            self.tests[bstack11l1ll1l_opy_] = {}
            self.bstack1l111l11_opy_.start()
            scopes = []
            driver = bstack1ll111ll_opy_(threading.current_thread(), bstack1lll11l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪএ"), None)
            current_thread = threading.current_thread()
            if not hasattr(current_thread, bstack1lll11l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡵࠪঐ")):
                current_thread.current_test_hooks = []
            current_thread.current_test_hooks.append(bstack11l1ll1l_opy_)
            if name in [bstack1lll11l_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ࠥ঑"), bstack1lll11l_opy_ (u"ࠢࡢࡨࡷࡩࡷࡥࡡ࡭࡮ࠥ঒")]:
                file_path = os.path.join(attrs.config.base_dir, attrs.config.environment_file)
                scopes = [attrs.config.environment_file]
            elif name in [bstack1lll11l_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡨࡨࡥࡹࡻࡲࡦࠤও"), bstack1lll11l_opy_ (u"ࠤࡤࡪࡹ࡫ࡲࡠࡨࡨࡥࡹࡻࡲࡦࠤঔ")]:
                file_path = attrs.filename
                scopes = [attrs.name]
            else:
                file_path = attrs.filename
                if hasattr(attrs, bstack1lll11l_opy_ (u"ࠪࡪࡪࡧࡴࡶࡴࡨࠫক")):
                    scopes =  [attrs.feature.name]
            hook_data = bstack1l111111_opy_(
                name=name,
                uuid=bstack11l1ll1l_opy_,
                started_at=bstack1l111lll_opy_(),
                file_path=file_path,
                framework=bstack1lll11l_opy_ (u"ࠦࡇ࡫ࡨࡢࡸࡨࠦখ"),
                bstack1l1l11l1_opy_=bstack1l111l1l_opy_.bstack1ll1l111_opy_(driver) if driver and driver.session_id else {},
                scope=scopes,
                result=bstack1lll11l_opy_ (u"ࠧࡶࡥ࡯ࡦ࡬ࡲ࡬ࠨগ"),
                hook_type=name
            )
            self.tests[bstack11l1ll1l_opy_][bstack1lll11l_opy_ (u"ࠨࡴࡦࡵࡷࡣࡩࡧࡴࡢࠤঘ")] = hook_data
            current_test_id = bstack1ll111ll_opy_(threading.current_thread(), bstack1lll11l_opy_ (u"ࠢࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠦঙ"), None)
            if current_test_id:
                hook_data.bstack11l111ll_opy_(current_test_id)
            if name == bstack1lll11l_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡣ࡯ࡰࠧচ"):
                threading.current_thread().before_all_hook_uuid = bstack11l1ll1l_opy_
            threading.current_thread().current_hook_uuid = bstack11l1ll1l_opy_
            bstack1l111l1l_opy_.bstack1lll1111_opy_(bstack1lll11l_opy_ (u"ࠤࡋࡳࡴࡱࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠥছ"), hook_data)
        except Exception as e:
            logger.debug(bstack1lll11l_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡲࡧࡨࡻࡲࡳࡧࡧࠤ࡮ࡴࠠࡴࡶࡤࡶࡹࠦࡨࡰࡱ࡮ࠤࡪࡼࡥ࡯ࡶࡶ࠰ࠥ࡮࡯ࡰ࡭ࠣࡲࡦࡳࡥ࠻ࠢࠨࡷ࠱ࠦࡥࡳࡴࡲࡶ࠿ࠦࠥࡴࠤজ"), name, e)
    def bstack11l11l11_opy_(self, attrs):
        bstack1l1111ll_opy_ = bstack1ll111ll_opy_(threading.current_thread(), bstack1lll11l_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨঝ"), None)
        hook_data = self.tests[bstack1l1111ll_opy_][bstack1lll11l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨঞ")]
        status = bstack1lll11l_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨট")
        exception = None
        bstack11l11ll1_opy_ = None
        if hook_data.name == bstack1lll11l_opy_ (u"ࠢࡢࡨࡷࡩࡷࡥࡡ࡭࡮ࠥঠ"):
            self.bstack1l111l11_opy_.reset()
            bstack11l111l1_opy_ = self.tests[bstack1ll111ll_opy_(threading.current_thread(), bstack1lll11l_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࡠࡣ࡯ࡰࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨড"), None)][bstack1lll11l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬঢ")].result.result
            if bstack11l111l1_opy_ == bstack1lll11l_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥণ"):
                if attrs.hook_failures == 1:
                    status = bstack1lll11l_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦত")
                elif attrs.hook_failures == 2:
                    status = bstack1lll11l_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧথ")
            elif attrs.aborted:
                status = bstack1lll11l_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨদ")
            threading.current_thread().before_all_hook_uuid = None
        else:
            if hook_data.name == bstack1lll11l_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࠫধ") and attrs.hook_failures == 1:
                status = bstack1lll11l_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣন")
            elif hasattr(attrs, bstack1lll11l_opy_ (u"ࠩࡨࡶࡷࡵࡲࡠ࡯ࡨࡷࡸࡧࡧࡦࠩ঩")) and attrs.error_message:
                status = bstack1lll11l_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥপ")
            bstack11l11ll1_opy_, exception = self._11l1llll_opy_(attrs)
        bstack1llll111_opy_ = Result(result=status, exception=exception, bstack11lll11l_opy_=[bstack11l11ll1_opy_])
        hook_data.stop(time=bstack1l111lll_opy_(), duration=0, result=bstack1llll111_opy_)
        bstack1l111l1l_opy_.bstack1lll1111_opy_(bstack1lll11l_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ফ"), self.tests[bstack1l1111ll_opy_][bstack1lll11l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨব")])
        threading.current_thread().current_hook_uuid = None
    def _11l1llll_opy_(self, attrs):
        try:
            import traceback
            bstack11l1l1l1_opy_ = traceback.format_tb(attrs.exc_traceback)
            bstack11l11ll1_opy_ = bstack11l1l1l1_opy_[-1] if bstack11l1l1l1_opy_ else None
            exception = attrs.exception
        except Exception:
            logger.debug(bstack1lll11l_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡵࡣࡤࡷࡵࡶࡪࡪࠠࡸࡪ࡬ࡰࡪࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡤࡷࡶࡸࡴࡳࠠࡵࡴࡤࡧࡪࡨࡡࡤ࡭ࠥভ"))
            bstack11l11ll1_opy_ = None
            exception = None
        return bstack11l11ll1_opy_, exception