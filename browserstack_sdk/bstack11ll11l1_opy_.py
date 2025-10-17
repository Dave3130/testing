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
import threading
import os
import logging
from uuid import uuid4
from bstack_utils.bstack1ll1ll11_opy_ import bstack1l11l1ll_opy_, bstack1ll1111l_opy_
from bstack_utils.bstack1l1lll11_opy_ import bstack11llll11_opy_
from bstack_utils.helper import bstack1l1lllll_opy_, bstack1l11llll_opy_, Result
from bstack_utils.bstack1llll1ll_opy_ import bstack1l11lll1_opy_
from bstack_utils.capture import bstack1lllll11_opy_
from bstack_utils.constants import *
logger = logging.getLogger(__name__)
class bstack11ll11l1_opy_:
    def __init__(self):
        self.bstack1ll1l11l_opy_ = bstack1lllll11_opy_(self.bstack1l1lll1l_opy_)
        self.tests = {}
    @staticmethod
    def bstack1l1lll1l_opy_(log):
        if not (log[bstack11111_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨॅ")] and log[bstack11111_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩॆ")].strip()):
            return
        active = bstack11llll11_opy_.bstack11lll1l1_opy_()
        log = {
            bstack11111_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨे"): log[bstack11111_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩै")],
            bstack11111_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧॉ"): bstack1l11llll_opy_(),
            bstack11111_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ॊ"): log[bstack11111_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧो")],
        }
        if active:
            if active[bstack11111_opy_ (u"ࠧࡵࡻࡳࡩࠬौ")] == bstack11111_opy_ (u"ࠨࡪࡲࡳࡰ्࠭"):
                log[bstack11111_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩॎ")] = active[bstack11111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪॏ")]
            elif active[bstack11111_opy_ (u"ࠫࡹࡿࡰࡦࠩॐ")] == bstack11111_opy_ (u"ࠬࡺࡥࡴࡶࠪ॑"):
                log[bstack11111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ॒࠭")] = active[bstack11111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ॓")]
        bstack1l11lll1_opy_.bstack11llllll_opy_([log])
    def start_test(self, attrs):
        test_uuid = uuid4().__str__()
        self.tests[test_uuid] = {}
        self.bstack1ll1l11l_opy_.start()
        driver = bstack1l1lllll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧ॔"), None)
        bstack1ll1ll11_opy_ = bstack1ll1111l_opy_(
            name=attrs.scenario.name,
            uuid=test_uuid,
            started_at=bstack1l11llll_opy_(),
            file_path=attrs.feature.filename,
            result=bstack11111_opy_ (u"ࠤࡳࡩࡳࡪࡩ࡯ࡩࠥॕ"),
            framework=bstack11111_opy_ (u"ࠪࡆࡪ࡮ࡡࡷࡧࠪॖ"),
            scope=[attrs.feature.name],
            bstack1lll11ll_opy_=bstack1l11lll1_opy_.bstack1l1l1lll_opy_(driver) if driver and driver.session_id else {},
            meta={},
            tags=attrs.scenario.tags
        )
        self.tests[test_uuid][bstack11111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧॗ")] = bstack1ll1ll11_opy_
        threading.current_thread().current_test_uuid = test_uuid
        bstack1l11lll1_opy_.bstack11llll1l_opy_(bstack11111_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭क़"), bstack1ll1ll11_opy_)
    def end_test(self, attrs):
        bstack11l1llll_opy_ = {
            bstack11111_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦख़"): attrs.feature.name,
            bstack11111_opy_ (u"ࠢࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠧग़"): attrs.feature.description
        }
        current_test_uuid = threading.current_thread().current_test_uuid
        bstack1ll1ll11_opy_ = self.tests[current_test_uuid][bstack11111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫज़")]
        meta = {
            bstack11111_opy_ (u"ࠤࡩࡩࡦࡺࡵࡳࡧࠥड़"): bstack11l1llll_opy_,
            bstack11111_opy_ (u"ࠥࡷࡹ࡫ࡰࡴࠤढ़"): bstack1ll1ll11_opy_.meta.get(bstack11111_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪफ़"), []),
            bstack11111_opy_ (u"ࠧࡹࡣࡦࡰࡤࡶ࡮ࡵࠢय़"): {
                bstack11111_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦॠ"): attrs.feature.scenarios[0].name if len(attrs.feature.scenarios) else None
            }
        }
        bstack1ll1ll11_opy_.bstack11ll1111_opy_(meta)
        bstack1ll1ll11_opy_.bstack11ll11ll_opy_(bstack1l1lllll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡷࠬॡ"), []))
        bstack11l1ll11_opy_, exception = self._11l1ll1l_opy_(attrs)
        bstack1lll1lll_opy_ = Result(result=attrs.status.name, exception=exception, bstack1l11ll11_opy_=[bstack11l1ll11_opy_])
        self.tests[threading.current_thread().current_test_uuid][bstack11111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫॢ")].stop(time=bstack1l11llll_opy_(), duration=int(attrs.duration)*1000, result=bstack1lll1lll_opy_)
        bstack1l11lll1_opy_.bstack11llll1l_opy_(bstack11111_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫॣ"), self.tests[threading.current_thread().current_test_uuid][bstack11111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭।")])
    def bstack11ll1lll_opy_(self, attrs):
        bstack1l1l1l11_opy_ = {
            bstack11111_opy_ (u"ࠫ࡮ࡪࠧ॥"): uuid4().__str__(),
            bstack11111_opy_ (u"ࠬࡱࡥࡺࡹࡲࡶࡩ࠭०"): attrs.keyword,
            bstack11111_opy_ (u"࠭ࡳࡵࡧࡳࡣࡦࡸࡧࡶ࡯ࡨࡲࡹ࠭१"): [],
            bstack11111_opy_ (u"ࠧࡵࡧࡻࡸࠬ२"): attrs.name,
            bstack11111_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬ३"): bstack1l11llll_opy_(),
            bstack11111_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩ४"): bstack11111_opy_ (u"ࠪࡴࡪࡴࡤࡪࡰࡪࠫ५"),
            bstack11111_opy_ (u"ࠫࡩ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠩ६"): bstack11111_opy_ (u"ࠬ࠭७")
        }
        self.tests[threading.current_thread().current_test_uuid][bstack11111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩ८")].add_step(bstack1l1l1l11_opy_)
        threading.current_thread().current_step_uuid = bstack1l1l1l11_opy_[bstack11111_opy_ (u"ࠧࡪࡦࠪ९")]
    def bstack11ll1l1l_opy_(self, attrs):
        current_test_id = bstack1l1lllll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬ॰"), None)
        current_step_uuid = bstack1l1lllll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡷࡹ࡫ࡰࡠࡷࡸ࡭ࡩ࠭ॱ"), None)
        bstack11l1ll11_opy_, exception = self._11l1ll1l_opy_(attrs)
        bstack1lll1lll_opy_ = Result(result=attrs.status.name, exception=exception, bstack1l11ll11_opy_=[bstack11l1ll11_opy_])
        self.tests[current_test_id][bstack11111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭ॲ")].bstack1l1l1111_opy_(current_step_uuid, duration=int(attrs.duration)*1000, result=bstack1lll1lll_opy_)
        threading.current_thread().current_step_uuid = None
    def bstack11l1lll1_opy_(self, name, attrs):
        try:
            bstack11ll1ll1_opy_ = uuid4().__str__()
            self.tests[bstack11ll1ll1_opy_] = {}
            self.bstack1ll1l11l_opy_.start()
            scopes = []
            driver = bstack1l1lllll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪॳ"), None)
            current_thread = threading.current_thread()
            if not hasattr(current_thread, bstack11111_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡵࠪॴ")):
                current_thread.current_test_hooks = []
            current_thread.current_test_hooks.append(bstack11ll1ll1_opy_)
            if name in [bstack11111_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ࠥॵ"), bstack11111_opy_ (u"ࠢࡢࡨࡷࡩࡷࡥࡡ࡭࡮ࠥॶ")]:
                file_path = os.path.join(attrs.config.base_dir, attrs.config.environment_file)
                scopes = [attrs.config.environment_file]
            elif name in [bstack11111_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡨࡨࡥࡹࡻࡲࡦࠤॷ"), bstack11111_opy_ (u"ࠤࡤࡪࡹ࡫ࡲࡠࡨࡨࡥࡹࡻࡲࡦࠤॸ")]:
                file_path = attrs.filename
                scopes = [attrs.name]
            else:
                file_path = attrs.filename
                if hasattr(attrs, bstack11111_opy_ (u"ࠪࡪࡪࡧࡴࡶࡴࡨࠫॹ")):
                    scopes =  [attrs.feature.name]
            hook_data = bstack1l11l1ll_opy_(
                name=name,
                uuid=bstack11ll1ll1_opy_,
                started_at=bstack1l11llll_opy_(),
                file_path=file_path,
                framework=bstack11111_opy_ (u"ࠦࡇ࡫ࡨࡢࡸࡨࠦॺ"),
                bstack1lll11ll_opy_=bstack1l11lll1_opy_.bstack1l1l1lll_opy_(driver) if driver and driver.session_id else {},
                scope=scopes,
                result=bstack11111_opy_ (u"ࠧࡶࡥ࡯ࡦ࡬ࡲ࡬ࠨॻ"),
                hook_type=name
            )
            self.tests[bstack11ll1ll1_opy_][bstack11111_opy_ (u"ࠨࡴࡦࡵࡷࡣࡩࡧࡴࡢࠤॼ")] = hook_data
            current_test_id = bstack1l1lllll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠢࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠦॽ"), None)
            if current_test_id:
                hook_data.bstack11ll1l11_opy_(current_test_id)
            if name == bstack11111_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡣ࡯ࡰࠧॾ"):
                threading.current_thread().before_all_hook_uuid = bstack11ll1ll1_opy_
            threading.current_thread().current_hook_uuid = bstack11ll1ll1_opy_
            bstack1l11lll1_opy_.bstack11llll1l_opy_(bstack11111_opy_ (u"ࠤࡋࡳࡴࡱࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠥॿ"), hook_data)
        except Exception as e:
            logger.debug(bstack11111_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡲࡧࡨࡻࡲࡳࡧࡧࠤ࡮ࡴࠠࡴࡶࡤࡶࡹࠦࡨࡰࡱ࡮ࠤࡪࡼࡥ࡯ࡶࡶ࠰ࠥ࡮࡯ࡰ࡭ࠣࡲࡦࡳࡥ࠻ࠢࠨࡷ࠱ࠦࡥࡳࡴࡲࡶ࠿ࠦࠥࡴࠤঀ"), name, e)
    def bstack11ll111l_opy_(self, attrs):
        bstack1l1ll1l1_opy_ = bstack1l1lllll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨঁ"), None)
        hook_data = self.tests[bstack1l1ll1l1_opy_][bstack11111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨং")]
        status = bstack11111_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨঃ")
        exception = None
        bstack11l1ll11_opy_ = None
        if hook_data.name == bstack11111_opy_ (u"ࠢࡢࡨࡷࡩࡷࡥࡡ࡭࡮ࠥ঄"):
            self.bstack1ll1l11l_opy_.reset()
            bstack11l1l1l1_opy_ = self.tests[bstack1l1lllll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࡠࡣ࡯ࡰࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨঅ"), None)][bstack11111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬআ")].result.result
            if bstack11l1l1l1_opy_ == bstack11111_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥই"):
                if attrs.hook_failures == 1:
                    status = bstack11111_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦঈ")
                elif attrs.hook_failures == 2:
                    status = bstack11111_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧউ")
            elif attrs.aborted:
                status = bstack11111_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨঊ")
            threading.current_thread().before_all_hook_uuid = None
        else:
            if hook_data.name == bstack11111_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࠫঋ") and attrs.hook_failures == 1:
                status = bstack11111_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣঌ")
            elif hasattr(attrs, bstack11111_opy_ (u"ࠩࡨࡶࡷࡵࡲࡠ࡯ࡨࡷࡸࡧࡧࡦࠩ঍")) and attrs.error_message:
                status = bstack11111_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥ঎")
            bstack11l1ll11_opy_, exception = self._11l1ll1l_opy_(attrs)
        bstack1lll1lll_opy_ = Result(result=status, exception=exception, bstack1l11ll11_opy_=[bstack11l1ll11_opy_])
        hook_data.stop(time=bstack1l11llll_opy_(), duration=0, result=bstack1lll1lll_opy_)
        bstack1l11lll1_opy_.bstack11llll1l_opy_(bstack11111_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭এ"), self.tests[bstack1l1ll1l1_opy_][bstack11111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨঐ")])
        threading.current_thread().current_hook_uuid = None
    def _11l1ll1l_opy_(self, attrs):
        try:
            import traceback
            bstack11l1l1ll_opy_ = traceback.format_tb(attrs.exc_traceback)
            bstack11l1ll11_opy_ = bstack11l1l1ll_opy_[-1] if bstack11l1l1ll_opy_ else None
            exception = attrs.exception
        except Exception:
            logger.debug(bstack11111_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡵࡣࡤࡷࡵࡶࡪࡪࠠࡸࡪ࡬ࡰࡪࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡤࡷࡶࡸࡴࡳࠠࡵࡴࡤࡧࡪࡨࡡࡤ࡭ࠥ঑"))
            bstack11l1ll11_opy_ = None
            exception = None
        return bstack11l1ll11_opy_, exception