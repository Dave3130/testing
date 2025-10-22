# coding: UTF-8
import sys
bstack111111l_opy_ = sys.version_info [0] == 2
bstack111lll_opy_ = 2048
bstack11ll111_opy_ = 7
def bstack11l1l11_opy_ (bstack1l11111_opy_):
    global bstack11l1ll1_opy_
    bstack1l1l111_opy_ = ord (bstack1l11111_opy_ [-1])
    bstack1lll11_opy_ = bstack1l11111_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1l1l111_opy_ % len (bstack1lll11_opy_)
    bstack1ll1l_opy_ = bstack1lll11_opy_ [:bstack1ll11l_opy_] + bstack1lll11_opy_ [bstack1ll11l_opy_:]
    if bstack111111l_opy_:
        bstack1ll1_opy_ = unicode () .join ([unichr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    else:
        bstack1ll1_opy_ = str () .join ([chr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    return eval (bstack1ll1_opy_)
import threading
import os
import logging
from uuid import uuid4
from bstack_utils.bstack1ll1l1l1_opy_ import bstack1l111l11_opy_, bstack1l11ll1l_opy_
from bstack_utils.bstack1lll11ll_opy_ import bstack1l1l11ll_opy_
from bstack_utils.helper import bstack1l111l1l_opy_, bstack1lllll11_opy_, Result
from bstack_utils.bstack1l11ll11_opy_ import bstack1ll1l11l_opy_
from bstack_utils.capture import bstack1l1ll111_opy_
from bstack_utils.constants import *
logger = logging.getLogger(__name__)
class bstack11l111l1_opy_:
    def __init__(self):
        self.bstack11lll11l_opy_ = bstack1l1ll111_opy_(self.bstack1ll1lll1_opy_)
        self.tests = {}
    @staticmethod
    def bstack1ll1lll1_opy_(log):
        if not (log[bstack11l1l11_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ२")] and log[bstack11l1l11_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ३")].strip()):
            return
        active = bstack1l1l11ll_opy_.bstack1l111lll_opy_()
        log = {
            bstack11l1l11_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ४"): log[bstack11l1l11_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩ५")],
            bstack11l1l11_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧ६"): bstack1lllll11_opy_(),
            bstack11l1l11_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭७"): log[bstack11l1l11_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ८")],
        }
        if active:
            if active[bstack11l1l11_opy_ (u"ࠧࡵࡻࡳࡩࠬ९")] == bstack11l1l11_opy_ (u"ࠨࡪࡲࡳࡰ࠭॰"):
                log[bstack11l1l11_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩॱ")] = active[bstack11l1l11_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪॲ")]
            elif active[bstack11l1l11_opy_ (u"ࠫࡹࡿࡰࡦࠩॳ")] == bstack11l1l11_opy_ (u"ࠬࡺࡥࡴࡶࠪॴ"):
                log[bstack11l1l11_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ॵ")] = active[bstack11l1l11_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧॶ")]
        bstack1ll1l11l_opy_.bstack1ll11l11_opy_([log])
    def start_test(self, attrs):
        test_uuid = uuid4().__str__()
        self.tests[test_uuid] = {}
        self.bstack11lll11l_opy_.start()
        driver = bstack1l111l1l_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧॷ"), None)
        bstack1ll1l1l1_opy_ = bstack1l11ll1l_opy_(
            name=attrs.scenario.name,
            uuid=test_uuid,
            started_at=bstack1lllll11_opy_(),
            file_path=attrs.feature.filename,
            result=bstack11l1l11_opy_ (u"ࠤࡳࡩࡳࡪࡩ࡯ࡩࠥॸ"),
            framework=bstack11l1l11_opy_ (u"ࠪࡆࡪ࡮ࡡࡷࡧࠪॹ"),
            scope=[attrs.feature.name],
            bstack1l1l1l1l_opy_=bstack1ll1l11l_opy_.bstack1ll1ll11_opy_(driver) if driver and driver.session_id else {},
            meta={},
            tags=attrs.scenario.tags
        )
        self.tests[test_uuid][bstack11l1l11_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧॺ")] = bstack1ll1l1l1_opy_
        threading.current_thread().current_test_uuid = test_uuid
        bstack1ll1l11l_opy_.bstack1l11lll1_opy_(bstack11l1l11_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭ॻ"), bstack1ll1l1l1_opy_)
    def end_test(self, attrs):
        bstack111llll1_opy_ = {
            bstack11l1l11_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦॼ"): attrs.feature.name,
            bstack11l1l11_opy_ (u"ࠢࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠧॽ"): attrs.feature.description
        }
        current_test_uuid = threading.current_thread().current_test_uuid
        bstack1ll1l1l1_opy_ = self.tests[current_test_uuid][bstack11l1l11_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫॾ")]
        meta = {
            bstack11l1l11_opy_ (u"ࠤࡩࡩࡦࡺࡵࡳࡧࠥॿ"): bstack111llll1_opy_,
            bstack11l1l11_opy_ (u"ࠥࡷࡹ࡫ࡰࡴࠤঀ"): bstack1ll1l1l1_opy_.meta.get(bstack11l1l11_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪঁ"), []),
            bstack11l1l11_opy_ (u"ࠧࡹࡣࡦࡰࡤࡶ࡮ࡵࠢং"): {
                bstack11l1l11_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦঃ"): attrs.feature.scenarios[0].name if len(attrs.feature.scenarios) else None
            }
        }
        bstack1ll1l1l1_opy_.bstack11l11111_opy_(meta)
        bstack1ll1l1l1_opy_.bstack11l1l1ll_opy_(bstack1l111l1l_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡷࠬ঄"), []))
        bstack11l1l11l_opy_, exception = self._11l1l111_opy_(attrs)
        bstack1l111ll1_opy_ = Result(result=attrs.status.name, exception=exception, bstack1ll111ll_opy_=[bstack11l1l11l_opy_])
        self.tests[threading.current_thread().current_test_uuid][bstack11l1l11_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫঅ")].stop(time=bstack1lllll11_opy_(), duration=int(attrs.duration)*1000, result=bstack1l111ll1_opy_)
        bstack1ll1l11l_opy_.bstack1l11lll1_opy_(bstack11l1l11_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫআ"), self.tests[threading.current_thread().current_test_uuid][bstack11l1l11_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭ই")])
    def bstack11l11ll1_opy_(self, attrs):
        bstack1l1lllll_opy_ = {
            bstack11l1l11_opy_ (u"ࠫ࡮ࡪࠧঈ"): uuid4().__str__(),
            bstack11l1l11_opy_ (u"ࠬࡱࡥࡺࡹࡲࡶࡩ࠭উ"): attrs.keyword,
            bstack11l1l11_opy_ (u"࠭ࡳࡵࡧࡳࡣࡦࡸࡧࡶ࡯ࡨࡲࡹ࠭ঊ"): [],
            bstack11l1l11_opy_ (u"ࠧࡵࡧࡻࡸࠬঋ"): attrs.name,
            bstack11l1l11_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬঌ"): bstack1lllll11_opy_(),
            bstack11l1l11_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩ঍"): bstack11l1l11_opy_ (u"ࠪࡴࡪࡴࡤࡪࡰࡪࠫ঎"),
            bstack11l1l11_opy_ (u"ࠫࡩ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠩএ"): bstack11l1l11_opy_ (u"ࠬ࠭ঐ")
        }
        self.tests[threading.current_thread().current_test_uuid][bstack11l1l11_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩ঑")].add_step(bstack1l1lllll_opy_)
        threading.current_thread().current_step_uuid = bstack1l1lllll_opy_[bstack11l1l11_opy_ (u"ࠧࡪࡦࠪ঒")]
    def bstack11l1l1l1_opy_(self, attrs):
        current_test_id = bstack1l111l1l_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬও"), None)
        current_step_uuid = bstack1l111l1l_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡷࡹ࡫ࡰࡠࡷࡸ࡭ࡩ࠭ঔ"), None)
        bstack11l1l11l_opy_, exception = self._11l1l111_opy_(attrs)
        bstack1l111ll1_opy_ = Result(result=attrs.status.name, exception=exception, bstack1ll111ll_opy_=[bstack11l1l11l_opy_])
        self.tests[current_test_id][bstack11l1l11_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭ক")].bstack1l1lll11_opy_(current_step_uuid, duration=int(attrs.duration)*1000, result=bstack1l111ll1_opy_)
        threading.current_thread().current_step_uuid = None
    def bstack11l11l1l_opy_(self, name, attrs):
        try:
            bstack11l11l11_opy_ = uuid4().__str__()
            self.tests[bstack11l11l11_opy_] = {}
            self.bstack11lll11l_opy_.start()
            scopes = []
            driver = bstack1l111l1l_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪখ"), None)
            current_thread = threading.current_thread()
            if not hasattr(current_thread, bstack11l1l11_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡵࠪগ")):
                current_thread.current_test_hooks = []
            current_thread.current_test_hooks.append(bstack11l11l11_opy_)
            if name in [bstack11l1l11_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ࠥঘ"), bstack11l1l11_opy_ (u"ࠢࡢࡨࡷࡩࡷࡥࡡ࡭࡮ࠥঙ")]:
                file_path = os.path.join(attrs.config.base_dir, attrs.config.environment_file)
                scopes = [attrs.config.environment_file]
            elif name in [bstack11l1l11_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡨࡨࡥࡹࡻࡲࡦࠤচ"), bstack11l1l11_opy_ (u"ࠤࡤࡪࡹ࡫ࡲࡠࡨࡨࡥࡹࡻࡲࡦࠤছ")]:
                file_path = attrs.filename
                scopes = [attrs.name]
            else:
                file_path = attrs.filename
                if hasattr(attrs, bstack11l1l11_opy_ (u"ࠪࡪࡪࡧࡴࡶࡴࡨࠫজ")):
                    scopes =  [attrs.feature.name]
            hook_data = bstack1l111l11_opy_(
                name=name,
                uuid=bstack11l11l11_opy_,
                started_at=bstack1lllll11_opy_(),
                file_path=file_path,
                framework=bstack11l1l11_opy_ (u"ࠦࡇ࡫ࡨࡢࡸࡨࠦঝ"),
                bstack1l1l1l1l_opy_=bstack1ll1l11l_opy_.bstack1ll1ll11_opy_(driver) if driver and driver.session_id else {},
                scope=scopes,
                result=bstack11l1l11_opy_ (u"ࠧࡶࡥ࡯ࡦ࡬ࡲ࡬ࠨঞ"),
                hook_type=name
            )
            self.tests[bstack11l11l11_opy_][bstack11l1l11_opy_ (u"ࠨࡴࡦࡵࡷࡣࡩࡧࡴࡢࠤট")] = hook_data
            current_test_id = bstack1l111l1l_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠢࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠦঠ"), None)
            if current_test_id:
                hook_data.bstack111lllll_opy_(current_test_id)
            if name == bstack11l1l11_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡣ࡯ࡰࠧড"):
                threading.current_thread().before_all_hook_uuid = bstack11l11l11_opy_
            threading.current_thread().current_hook_uuid = bstack11l11l11_opy_
            bstack1ll1l11l_opy_.bstack1l11lll1_opy_(bstack11l1l11_opy_ (u"ࠤࡋࡳࡴࡱࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠥঢ"), hook_data)
        except Exception as e:
            logger.debug(bstack11l1l11_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡲࡧࡨࡻࡲࡳࡧࡧࠤ࡮ࡴࠠࡴࡶࡤࡶࡹࠦࡨࡰࡱ࡮ࠤࡪࡼࡥ࡯ࡶࡶ࠰ࠥ࡮࡯ࡰ࡭ࠣࡲࡦࡳࡥ࠻ࠢࠨࡷ࠱ࠦࡥࡳࡴࡲࡶ࠿ࠦࠥࡴࠤণ"), name, e)
    def bstack11l1111l_opy_(self, attrs):
        bstack1l1ll1ll_opy_ = bstack1l111l1l_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨত"), None)
        hook_data = self.tests[bstack1l1ll1ll_opy_][bstack11l1l11_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨথ")]
        status = bstack11l1l11_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨদ")
        exception = None
        bstack11l1l11l_opy_ = None
        if hook_data.name == bstack11l1l11_opy_ (u"ࠢࡢࡨࡷࡩࡷࡥࡡ࡭࡮ࠥধ"):
            self.bstack11lll11l_opy_.reset()
            bstack11l111ll_opy_ = self.tests[bstack1l111l1l_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࡠࡣ࡯ࡰࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨন"), None)][bstack11l1l11_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬ঩")].result.result
            if bstack11l111ll_opy_ == bstack11l1l11_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥপ"):
                if attrs.hook_failures == 1:
                    status = bstack11l1l11_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦফ")
                elif attrs.hook_failures == 2:
                    status = bstack11l1l11_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧব")
            elif attrs.aborted:
                status = bstack11l1l11_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨভ")
            threading.current_thread().before_all_hook_uuid = None
        else:
            if hook_data.name == bstack11l1l11_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࠫম") and attrs.hook_failures == 1:
                status = bstack11l1l11_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣয")
            elif hasattr(attrs, bstack11l1l11_opy_ (u"ࠩࡨࡶࡷࡵࡲࡠ࡯ࡨࡷࡸࡧࡧࡦࠩর")) and attrs.error_message:
                status = bstack11l1l11_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥ঱")
            bstack11l1l11l_opy_, exception = self._11l1l111_opy_(attrs)
        bstack1l111ll1_opy_ = Result(result=status, exception=exception, bstack1ll111ll_opy_=[bstack11l1l11l_opy_])
        hook_data.stop(time=bstack1lllll11_opy_(), duration=0, result=bstack1l111ll1_opy_)
        bstack1ll1l11l_opy_.bstack1l11lll1_opy_(bstack11l1l11_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ল"), self.tests[bstack1l1ll1ll_opy_][bstack11l1l11_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨ঳")])
        threading.current_thread().current_hook_uuid = None
    def _11l1l111_opy_(self, attrs):
        try:
            import traceback
            bstack11l11lll_opy_ = traceback.format_tb(attrs.exc_traceback)
            bstack11l1l11l_opy_ = bstack11l11lll_opy_[-1] if bstack11l11lll_opy_ else None
            exception = attrs.exception
        except Exception:
            logger.debug(bstack11l1l11_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡵࡣࡤࡷࡵࡶࡪࡪࠠࡸࡪ࡬ࡰࡪࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡤࡷࡶࡸࡴࡳࠠࡵࡴࡤࡧࡪࡨࡡࡤ࡭ࠥ঴"))
            bstack11l1l11l_opy_ = None
            exception = None
        return bstack11l1l11l_opy_, exception