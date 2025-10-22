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
from datetime import datetime, timezone
from uuid import uuid4
from typing import Dict, List, Any, Tuple
from browserstack_sdk.sdk_cli.bstack1ll1lllll1l_opy_ import bstack1ll1ll11l1l_opy_
from browserstack_sdk.sdk_cli.utils.bstack11l111111_opy_ import bstack1ll111l111l_opy_
from pathlib import Path
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.test_framework import (
    TestFramework,
    bstack1lll11l1lll_opy_,
    bstack1lll1lll1ll_opy_,
    bstack1llll111111_opy_,
    bstack1l1llll1111_opy_,
    bstack1ll111llll1_opy_,
)
import traceback
from bstack_utils.helper import bstack1ll11lll11l_opy_
from bstack_utils.bstack1l11l1l11_opy_ import bstack1llllll11ll_opy_
from bstack_utils.constants import EVENTS
from browserstack_sdk.sdk_cli.utils.bstack1ll1l111l11_opy_ import bstack1ll11l1llll_opy_
from browserstack_sdk.sdk_cli.bstack1lll11l1l11_opy_ import bstack1lll11l11ll_opy_
bstack1ll1l11lll1_opy_ = bstack1ll11lll11l_opy_()
bstack1l1lll1ll1l_opy_ = bstack111l1l_opy_ (u"࡙ࠥࡵࡲ࡯ࡢࡦࡨࡨࡆࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࡴ࠯ࠥሖ")
bstack1l1llllll1l_opy_ = bstack111l1l_opy_ (u"ࠦࡍࡵ࡯࡬ࡎࡨࡺࡪࡲࠢሗ")
bstack1ll11l1lll1_opy_ = bstack111l1l_opy_ (u"ࠧࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࡊࡲࡳࡰࡋࡶࡦࡰࡷࠦመ")
bstack1l1lllll111_opy_ = 1.0
_1ll11llll1l_opy_ = set()
class PytestBDDFramework(TestFramework):
    bstack1l1lllll1l1_opy_ = bstack111l1l_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡫࡯ࡸࡵࡷࡵࡩࡸࠨሙ")
    bstack1ll1111l111_opy_ = bstack111l1l_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡶࡣࡸࡺࡡࡳࡶࡨࡨࠧሚ")
    bstack1ll111ll1l1_opy_ = bstack111l1l_opy_ (u"ࠣࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡷࡤ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪࠢማ")
    bstack1ll1l111l1l_opy_ = bstack111l1l_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡲࡡࡴࡶࡢࡷࡹࡧࡲࡵࡧࡧࠦሜ")
    bstack1ll111l1l11_opy_ = bstack111l1l_opy_ (u"ࠥࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥ࡬ࡢࡵࡷࡣ࡫࡯࡮ࡪࡵ࡫ࡩࡩࠨም")
    bstack1l1llll11l1_opy_: bool
    bstack1lll11l1l11_opy_: bstack1lll11l11ll_opy_  = None
    bstack1ll11l11l1l_opy_ = [
        bstack1lll11l1lll_opy_.BEFORE_ALL,
        bstack1lll11l1lll_opy_.AFTER_ALL,
        bstack1lll11l1lll_opy_.BEFORE_EACH,
        bstack1lll11l1lll_opy_.AFTER_EACH,
    ]
    def __init__(
        self,
        bstack1ll1l111lll_opy_: Dict[str, str],
        bstack1l1lll1l1ll_opy_: List[str]=[bstack111l1l_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠣሞ")],
        bstack1lll11l1l11_opy_: bstack1lll11l11ll_opy_ = None,
        bstack1llll11ll11_opy_=None
    ):
        super().__init__(bstack1l1lll1l1ll_opy_, bstack1ll1l111lll_opy_, bstack1lll11l1l11_opy_)
        self.bstack1l1llll11l1_opy_ = any(bstack111l1l_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠤሟ") in item.lower() for item in bstack1l1lll1l1ll_opy_)
        self.bstack1llll11ll11_opy_ = bstack1llll11ll11_opy_
    def track_event(
        self,
        context: bstack1l1llll1111_opy_,
        test_framework_state: bstack1lll11l1lll_opy_,
        test_hook_state: bstack1llll111111_opy_,
        *args,
        **kwargs,
    ):
        super().track_event(self, context, test_framework_state, test_hook_state, *args, **kwargs)
        if test_framework_state == bstack1lll11l1lll_opy_.TEST or test_framework_state in PytestBDDFramework.bstack1ll11l11l1l_opy_:
            bstack1ll111l111l_opy_(test_framework_state, test_hook_state)
        if test_framework_state == bstack1lll11l1lll_opy_.NONE:
            self.logger.warning(bstack111l1l_opy_ (u"ࠨࡩࡨࡰࡲࡶࡪࡪࠠࡤࡣ࡯ࡰࡧࡧࡣ࡬ࠢࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀࠤࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࡃࠢሠ") + str(test_hook_state) + bstack111l1l_opy_ (u"ࠢࠣሡ"))
            return
        if not self.bstack1l1llll11l1_opy_:
            self.logger.warning(bstack111l1l_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡦࡸࡨࡲࡹࡀࠠࡶࡰࡶࡹࡵࡶ࡯ࡳࡶࡨࡨࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫࠾ࠤሢ") + str(str(self.bstack1l1lll1l1ll_opy_)) + bstack111l1l_opy_ (u"ࠤࠥሣ"))
            return
        if not isinstance(args, tuple) or len(args) == 0:
            self.logger.warning(bstack111l1l_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡨࡺࡪࡴࡴ࠻ࠢࡸࡲࡪࡾࡰࡦࡥࡷࡩࡩࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧሤ") + str(kwargs) + bstack111l1l_opy_ (u"ࠦࠧሥ"))
            return
        instance = self.__1ll11l11111_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        if not instance:
            self.logger.debug(bstack111l1l_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡺࡴࡨࡢࡰࡧࡰࡪࡪࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࡽࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࢁࠥࡧࡲࡨࡵࡀࠦሦ") + str(args) + bstack111l1l_opy_ (u"ࠨࠢሧ"))
            return
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1ll11l11l1l_opy_ and test_hook_state == bstack1llll111111_opy_.PRE:
                bstack1ll11l11lll_opy_ = bstack1llllll11ll_opy_.bstack1ll11lllll1_opy_(EVENTS.bstack1l111lllll_opy_.value)
                name = str(EVENTS.bstack1l111lllll_opy_.name)+bstack111l1l_opy_ (u"ࠢ࠻ࠤረ")+str(test_framework_state.name)
                TestFramework.bstack1ll111ll111_opy_(instance, name, bstack1ll11l11lll_opy_)
        except Exception as e:
            self.logger.debug(bstack111l1l_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡩࡱࡲ࡯ࠥ࡫ࡲࡳࡱࡵࠤࡵࡸࡥ࠻ࠢࡾࢁࠧሩ").format(e))
        try:
            if test_framework_state == bstack1lll11l1lll_opy_.TEST:
                if not TestFramework.bstack1llll1l1l11_opy_(instance, TestFramework.bstack1l1lll1l1l1_opy_) and test_hook_state == bstack1llll111111_opy_.PRE:
                    if not (len(args) >= 3):
                        return
                    test = PytestBDDFramework.__1ll1111llll_opy_(args)
                    if test:
                        instance.data.update(test)
                        self.logger.debug(bstack111l1l_opy_ (u"ࠤ࡯ࡳࡦࡪࡥࡥࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࢀ࡯࡮ࡴࡶࡤࡲࡨ࡫࠮ࡳࡧࡩࠬ࠮ࢃࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࠤሪ") + str(test_hook_state) + bstack111l1l_opy_ (u"ࠥࠦራ"))
                if test_hook_state == bstack1llll111111_opy_.PRE and not TestFramework.bstack1llll1l1l11_opy_(instance, TestFramework.bstack1ll1l111111_opy_):
                    TestFramework.bstack1llll1l111l_opy_(instance, TestFramework.bstack1ll1l111111_opy_, datetime.now(tz=timezone.utc))
                    PytestBDDFramework.__1ll11l1l1ll_opy_(instance, args)
                    self.logger.debug(bstack111l1l_opy_ (u"ࠦࡸ࡫ࡴࠡࡶࡨࡷࡹ࠳ࡳࡵࡣࡵࡸࠥ࡬࡯ࡳࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࢀ࡯࡮ࡴࡶࡤࡲࡨ࡫࠮ࡳࡧࡩࠬ࠮ࢃࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࠤሬ") + str(test_hook_state) + bstack111l1l_opy_ (u"ࠧࠨር"))
                elif test_hook_state == bstack1llll111111_opy_.POST and not TestFramework.bstack1llll1l1l11_opy_(instance, TestFramework.bstack1ll1111ll1l_opy_):
                    TestFramework.bstack1llll1l111l_opy_(instance, TestFramework.bstack1ll1111ll1l_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack111l1l_opy_ (u"ࠨࡳࡦࡶࠣࡸࡪࡹࡴ࠮ࡧࡱࡨࠥ࡬࡯ࡳࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࢀ࡯࡮ࡴࡶࡤࡲࡨ࡫࠮ࡳࡧࡩࠬ࠮ࢃࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࠤሮ") + str(test_hook_state) + bstack111l1l_opy_ (u"ࠢࠣሯ"))
            elif test_framework_state == bstack1lll11l1lll_opy_.STEP:
                if test_hook_state == bstack1llll111111_opy_.PRE:
                    PytestBDDFramework.__1ll1l1l1111_opy_(instance, args)
                elif test_hook_state == bstack1llll111111_opy_.POST:
                    PytestBDDFramework.__1ll111lll11_opy_(instance, args)
            elif test_framework_state == bstack1lll11l1lll_opy_.LOG and test_hook_state == bstack1llll111111_opy_.POST:
                PytestBDDFramework.__1l1llll1lll_opy_(instance, *args)
            elif test_framework_state == bstack1lll11l1lll_opy_.LOG_REPORT and test_hook_state == bstack1llll111111_opy_.POST:
                self.__1ll1l1ll111_opy_(instance, *args)
                self.__1ll1l1111l1_opy_(instance)
            elif test_framework_state in PytestBDDFramework.bstack1ll11l11l1l_opy_:
                self.__1ll11ll1lll_opy_(instance, test_framework_state, test_hook_state, *args)
            self.logger.debug(bstack111l1l_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡦࡸࡨࡲࡹࡀࠠࡩࡣࡱࡨࡱ࡫ࡤࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࡾࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࢂࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࠤሰ") + str(instance.ref()) + bstack111l1l_opy_ (u"ࠤࠥሱ"))
        except Exception as e:
            self.logger.error(e)
            traceback.print_exc()
        self.bstack1ll11ll1l1l_opy_(instance, (test_framework_state, test_hook_state), *args, **kwargs)
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1ll11l11l1l_opy_ and test_hook_state == bstack1llll111111_opy_.POST:
                name = str(EVENTS.bstack1l111lllll_opy_.name)+bstack111l1l_opy_ (u"ࠥ࠾ࠧሲ")+str(test_framework_state.name)
                bstack1ll11l11lll_opy_ = TestFramework.bstack1l1lllll11l_opy_(instance, name)
                bstack1llllll11ll_opy_.end(EVENTS.bstack1l111lllll_opy_.value, bstack1ll11l11lll_opy_+bstack111l1l_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦሳ"), bstack1ll11l11lll_opy_+bstack111l1l_opy_ (u"ࠧࡀࡥ࡯ࡦࠥሴ"), True, None, test_framework_state.name)
        except Exception as e:
            self.logger.debug(bstack111l1l_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡮࡯ࡰ࡭ࠣࡩࡷࡸ࡯ࡳ࠼ࠣࡿࢂࠨስ").format(e))
    def bstack1ll111111l1_opy_(self):
        return self.bstack1l1llll11l1_opy_
    def __1l1llll1ll1_opy_(self, *args):
        if len(args) > 2 and callable(getattr(args[2], bstack111l1l_opy_ (u"ࠢࡨࡧࡷࡣࡷ࡫ࡳࡶ࡮ࡷࠦሶ"), None)):
            rep = args[2].get_result()
            if rep:
                return TestFramework.bstack1ll111l1lll_opy_(rep, [bstack111l1l_opy_ (u"ࠣࡹ࡫ࡩࡳࠨሷ"), bstack111l1l_opy_ (u"ࠤࡲࡹࡹࡩ࡯࡮ࡧࠥሸ"), bstack111l1l_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥሹ"), bstack111l1l_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦሺ"), bstack111l1l_opy_ (u"ࠧࡹ࡫ࡪࡲࡳࡩࡩࠨሻ"), bstack111l1l_opy_ (u"ࠨ࡬ࡰࡰࡪࡶࡪࡶࡲࡵࡧࡻࡸࠧሼ")])
        return None
    def __1ll1l1ll111_opy_(self, instance: bstack1lll1lll1ll_opy_, *args):
        result = self.__1l1llll1ll1_opy_(*args)
        if not result:
            return
        failure = None
        bstack1111111l1l_opy_ = None
        if result.get(bstack111l1l_opy_ (u"ࠢࡰࡷࡷࡧࡴࡳࡥࠣሽ"), None) == bstack111l1l_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣሾ") and len(args) > 1 and getattr(args[1], bstack111l1l_opy_ (u"ࠤࡨࡼࡨ࡯࡮ࡧࡱࠥሿ"), None) is not None:
            failure = [{bstack111l1l_opy_ (u"ࠪࡦࡦࡩ࡫ࡵࡴࡤࡧࡪ࠭ቀ"): [args[1].excinfo.exconly(), result.get(bstack111l1l_opy_ (u"ࠦࡱࡵ࡮ࡨࡴࡨࡴࡷࡺࡥࡹࡶࠥቁ"), None)]}]
            bstack1111111l1l_opy_ = bstack111l1l_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࡆࡴࡵࡳࡷࠨቂ") if bstack111l1l_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࠤቃ") in getattr(args[1].excinfo, bstack111l1l_opy_ (u"ࠢࡵࡻࡳࡩࡳࡧ࡭ࡦࠤቄ"), bstack111l1l_opy_ (u"ࠣࠤቅ")) else bstack111l1l_opy_ (u"ࠤࡘࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡊࡸࡲࡰࡴࠥቆ")
        bstack1ll1l1l1lll_opy_ = result.get(bstack111l1l_opy_ (u"ࠥࡳࡺࡺࡣࡰ࡯ࡨࠦቇ"), TestFramework.bstack1ll1l11l111_opy_)
        if bstack1ll1l1l1lll_opy_ != TestFramework.bstack1ll1l11l111_opy_:
            TestFramework.bstack1llll1l111l_opy_(instance, TestFramework.bstack1ll11ll11ll_opy_, datetime.now(tz=timezone.utc))
        TestFramework.bstack1ll111111ll_opy_(instance, {
            TestFramework.bstack1lll1ll11ll_opy_: failure,
            TestFramework.bstack1ll11l11ll1_opy_: bstack1111111l1l_opy_,
            TestFramework.bstack1lll1ll1l1l_opy_: bstack1ll1l1l1lll_opy_,
        })
    def __1ll11l11111_opy_(
        self,
        context: bstack1l1llll1111_opy_,
        test_framework_state: bstack1lll11l1lll_opy_,
        test_hook_state: bstack1llll111111_opy_,
        *args,
        **kwargs,
    ):
        instance = None
        if test_framework_state == bstack1lll11l1lll_opy_.SETUP_FIXTURE:
            instance = self.__1ll111l11l1_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        else:
            target = None # bstack1ll11ll1l11_opy_ bstack1ll11ll1ll1_opy_ this to be bstack111l1l_opy_ (u"ࠦࡳࡵࡤࡦ࡫ࡧࠦቈ")
            if test_framework_state == bstack1lll11l1lll_opy_.INIT_TEST:
                target = args[0] if isinstance(args[0], str) else None
                if target:
                    self.__1ll11111ll1_opy_(context, test_framework_state, target, *args)
            elif test_framework_state == bstack1lll11l1lll_opy_.LOG:
                nodeid = getattr(getattr(args[0], bstack111l1l_opy_ (u"ࠧࡴ࡯ࡥࡧࠥ቉"), None), bstack111l1l_opy_ (u"ࠨ࡮ࡰࡦࡨ࡭ࡩࠨቊ"), None) if args else None
                if isinstance(nodeid, str):
                    target = nodeid
            elif getattr(args[0], bstack111l1l_opy_ (u"ࠢ࡯ࡱࡧࡩࠧቋ"), None):
                target = args[0].node.nodeid
            elif getattr(args[0], bstack111l1l_opy_ (u"ࠣࡰࡲࡨࡪ࡯ࡤࠣቌ"), None):
                target = args[0].nodeid
            instance = TestFramework.bstack1l1llll111l_opy_(target) if target else None
        return instance
    def __1ll11ll1lll_opy_(
        self,
        instance: bstack1lll1lll1ll_opy_,
        test_framework_state: bstack1lll11l1lll_opy_,
        test_hook_state: bstack1llll111111_opy_,
        *args,
    ):
        key = test_framework_state.name
        bstack1ll1l11l11l_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll1111l111_opy_, {})
        if not key in bstack1ll1l11l11l_opy_:
            bstack1ll1l11l11l_opy_[key] = []
        bstack1ll11lll1ll_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll111ll1l1_opy_, {})
        if not key in bstack1ll11lll1ll_opy_:
            bstack1ll11lll1ll_opy_[key] = []
        bstack1l1llll1l1l_opy_ = {
            PytestBDDFramework.bstack1ll1111l111_opy_: bstack1ll1l11l11l_opy_,
            PytestBDDFramework.bstack1ll111ll1l1_opy_: bstack1ll11lll1ll_opy_,
        }
        if test_hook_state == bstack1llll111111_opy_.PRE:
            hook_name = args[1] if len(args) > 1 else None
            hook = {
                bstack111l1l_opy_ (u"ࠤ࡮ࡩࡾࠨቍ"): key,
                TestFramework.bstack1ll11lll1l1_opy_: uuid4().__str__(),
                TestFramework.bstack1ll1l11llll_opy_: TestFramework.bstack1ll111ll11l_opy_,
                TestFramework.bstack1ll11l111ll_opy_: datetime.now(tz=timezone.utc),
                TestFramework.bstack1ll1l1l111l_opy_: [],
                TestFramework.bstack1ll1111l1ll_opy_: hook_name,
                TestFramework.bstack1ll11l1l11l_opy_: bstack1ll11l1llll_opy_.bstack1ll1l1l11l1_opy_()
            }
            bstack1ll1l11l11l_opy_[key].append(hook)
            bstack1l1llll1l1l_opy_[PytestBDDFramework.bstack1ll1l111l1l_opy_] = key
        elif test_hook_state == bstack1llll111111_opy_.POST:
            bstack1ll11l111l1_opy_ = bstack1ll1l11l11l_opy_.get(key, [])
            hook = bstack1ll11l111l1_opy_.pop() if bstack1ll11l111l1_opy_ else None
            if hook:
                result = self.__1l1llll1ll1_opy_(*args)
                if result:
                    bstack1ll1l1l1l1l_opy_ = result.get(bstack111l1l_opy_ (u"ࠥࡳࡺࡺࡣࡰ࡯ࡨࠦ቎"), TestFramework.bstack1ll111ll11l_opy_)
                    if bstack1ll1l1l1l1l_opy_ != TestFramework.bstack1ll111ll11l_opy_:
                        hook[TestFramework.bstack1ll1l11llll_opy_] = bstack1ll1l1l1l1l_opy_
                hook[TestFramework.bstack1ll1l11l1ll_opy_] = datetime.now(tz=timezone.utc)
                hook[TestFramework.bstack1ll11l1l11l_opy_] = bstack1ll11l1llll_opy_.bstack1ll1l1l11l1_opy_()
                self.bstack1ll1l11ll11_opy_(hook)
                logs = hook.get(TestFramework.bstack1ll11lll111_opy_, [])
                self.bstack1ll11llllll_opy_(instance, logs)
                bstack1ll11lll1ll_opy_[key].append(hook)
                bstack1l1llll1l1l_opy_[PytestBDDFramework.bstack1ll111l1l11_opy_] = key
        TestFramework.bstack1ll111111ll_opy_(instance, bstack1l1llll1l1l_opy_)
        self.logger.debug(bstack111l1l_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢ࡬ࡴࡵ࡫ࡠࡧࡹࡩࡳࡺ࠺ࠡࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࡀࡿࡰ࡫ࡹࡾ࠰ࡾࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࢂࠦࡨࡰࡱ࡮ࡷࡤࡹࡴࡢࡴࡷࡩࡩࡃࡻࡩࡱࡲ࡯ࡸࡥࡳࡵࡣࡵࡸࡪࡪࡽࠡࡪࡲࡳࡰࡹ࡟ࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥ࠿ࠥ቏") + str(bstack1ll11lll1ll_opy_) + bstack111l1l_opy_ (u"ࠧࠨቐ"))
    def __1ll111l11l1_opy_(
        self,
        context: bstack1l1llll1111_opy_,
        test_framework_state: bstack1lll11l1lll_opy_,
        test_hook_state: bstack1llll111111_opy_,
        *args,
        **kwargs,
    ):
        fixturedef = TestFramework.bstack1ll111l1lll_opy_(args[0], [bstack111l1l_opy_ (u"ࠨࡳࡤࡱࡳࡩࠧቑ"), bstack111l1l_opy_ (u"ࠢࡢࡴࡪࡲࡦࡳࡥࠣቒ"), bstack111l1l_opy_ (u"ࠣࡲࡤࡶࡦࡳࡳࠣቓ"), bstack111l1l_opy_ (u"ࠤ࡬ࡨࡸࠨቔ"), bstack111l1l_opy_ (u"ࠥࡹࡳ࡯ࡴࡵࡧࡶࡸࠧቕ"), bstack111l1l_opy_ (u"ࠦࡧࡧࡳࡦ࡫ࡧࠦቖ")]) if len(args) > 0 else {}
        request = args[1] if len(args) > 1 else None
        scenario = args[2] if len(args) == 3 else None
        scope = request.scope if hasattr(request, bstack111l1l_opy_ (u"ࠧࡹࡣࡰࡲࡨࠦ቗")) else fixturedef.get(bstack111l1l_opy_ (u"ࠨࡳࡤࡱࡳࡩࠧቘ"), None)
        fixturename = request.fixturename if hasattr(request, bstack111l1l_opy_ (u"ࠢࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࠧ቙")) else None
        node = request.node if hasattr(request, bstack111l1l_opy_ (u"ࠣࡰࡲࡨࡪࠨቚ")) else None
        target = request.node.nodeid if hasattr(node, bstack111l1l_opy_ (u"ࠤࡱࡳࡩ࡫ࡩࡥࠤቛ")) else None
        baseid = fixturedef.get(bstack111l1l_opy_ (u"ࠥࡦࡦࡹࡥࡪࡦࠥቜ"), None) or bstack111l1l_opy_ (u"ࠦࠧቝ")
        if (not target or len(baseid) > 0) and hasattr(request, bstack111l1l_opy_ (u"ࠧࡥࡰࡺࡨࡸࡲࡨ࡯ࡴࡦ࡯ࠥ቞")):
            target = PytestBDDFramework.__1l1lll1ll11_opy_(request._pyfuncitem.location) if hasattr(request._pyfuncitem, bstack111l1l_opy_ (u"ࠨ࡬ࡰࡥࡤࡸ࡮ࡵ࡮ࠣ቟")) else None
            if target and not TestFramework.bstack1l1llll111l_opy_(target):
                self.__1ll11111ll1_opy_(context, test_framework_state, target, (target, request._pyfuncitem.location))
                node = request._pyfuncitem
                self.logger.debug(bstack111l1l_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡦࡪࡺࡷࡹࡷ࡫࡟ࡦࡸࡨࡲࡹࡀࠠࡧࡣ࡯ࡰࡧࡧࡣ࡬ࠢࡷࡥࡷ࡭ࡥࡵ࠿ࡾࡸࡦࡸࡧࡦࡶࢀࠤ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦ࠿ࡾࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥࡾࠢࡱࡳࡩ࡫࠽ࡼࡰࡲࡨࡪࢃࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࠤበ") + str(test_hook_state) + bstack111l1l_opy_ (u"ࠣࠤቡ"))
        if not fixturedef or not scope or not target:
            self.logger.warning(bstack111l1l_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡨ࡬ࡼࡹࡻࡲࡦࡡࡨࡺࡪࡴࡴ࠻ࠢࡸࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࠥ࡫ࡶࡦࡰࡷࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂ࠴ࡻࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦࡿࠣࡪ࡮ࡾࡴࡶࡴࡨࡨࡪ࡬࠽ࡼࡨ࡬ࡼࡹࡻࡲࡦࡦࡨࡪࢂࠦࡳࡤࡱࡳࡩࡂࢁࡳࡤࡱࡳࡩࢂࠦࡴࡢࡴࡪࡩࡹࡃࠢቢ") + str(target) + bstack111l1l_opy_ (u"ࠥࠦባ"))
            return None
        instance = TestFramework.bstack1l1llll111l_opy_(target)
        if not instance:
            self.logger.warning(bstack111l1l_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡪ࡮ࡾࡴࡶࡴࡨࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡺࡴࡨࡢࡰࡧࡰࡪࡪࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࡽࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࢁࠥ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࡀࡿ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦࡿࠣࡷࡨࡵࡰࡦ࠿ࡾࡷࡨࡵࡰࡦࡿࠣࡦࡦࡹࡥࡪࡦࡀࡿࡧࡧࡳࡦ࡫ࡧࢁࠥࡺࡡࡳࡩࡨࡸࡂࠨቤ") + str(target) + bstack111l1l_opy_ (u"ࠧࠨብ"))
            return None
        bstack1ll11111l1l_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1l1lllll1l1_opy_, {})
        if os.getenv(bstack111l1l_opy_ (u"ࠨࡓࡅࡍࡢࡇࡑࡏ࡟ࡇࡎࡄࡋࡤࡌࡉ࡙ࡖࡘࡖࡊ࡙ࠢቦ"), bstack111l1l_opy_ (u"ࠢ࠲ࠤቧ")) == bstack111l1l_opy_ (u"ࠣ࠳ࠥቨ"):
            bstack1ll111l1l1l_opy_ = bstack111l1l_opy_ (u"ࠤ࠽ࠦቩ").join((scope, fixturename))
            bstack1ll11111111_opy_ = datetime.now(tz=timezone.utc)
            bstack1l1lll1llll_opy_ = {
                bstack111l1l_opy_ (u"ࠥ࡯ࡪࡿࠢቪ"): bstack1ll111l1l1l_opy_,
                bstack111l1l_opy_ (u"ࠦࡹࡧࡧࡴࠤቫ"): PytestBDDFramework.__1ll11111l11_opy_(request.node, scenario),
                bstack111l1l_opy_ (u"ࠧ࡬ࡩࡹࡶࡸࡶࡪࠨቬ"): fixturedef,
                bstack111l1l_opy_ (u"ࠨࡳࡤࡱࡳࡩࠧቭ"): scope,
                bstack111l1l_opy_ (u"ࠢࡵࡻࡳࡩࠧቮ"): None,
            }
            try:
                if test_hook_state == bstack1llll111111_opy_.POST and callable(getattr(args[-1], bstack111l1l_opy_ (u"ࠣࡩࡨࡸࡤࡸࡥࡴࡷ࡯ࡸࠧቯ"), None)):
                    bstack1l1lll1llll_opy_[bstack111l1l_opy_ (u"ࠤࡷࡽࡵ࡫ࠢተ")] = TestFramework.bstack1l1llll1l11_opy_(args[-1].get_result())
            except Exception as e:
                pass
            if test_hook_state == bstack1llll111111_opy_.PRE:
                bstack1l1lll1llll_opy_[bstack111l1l_opy_ (u"ࠥࡹࡺ࡯ࡤࠣቱ")] = uuid4().__str__()
                bstack1l1lll1llll_opy_[PytestBDDFramework.bstack1ll11l111ll_opy_] = bstack1ll11111111_opy_
            elif test_hook_state == bstack1llll111111_opy_.POST:
                bstack1l1lll1llll_opy_[PytestBDDFramework.bstack1ll1l11l1ll_opy_] = bstack1ll11111111_opy_
            if bstack1ll111l1l1l_opy_ in bstack1ll11111l1l_opy_:
                bstack1ll11111l1l_opy_[bstack1ll111l1l1l_opy_].update(bstack1l1lll1llll_opy_)
                self.logger.debug(bstack111l1l_opy_ (u"ࠦࡺࡶࡤࡢࡶࡨࡨࠥ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࡀࡿ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦࡿࠣࡷࡨࡵࡰࡦ࠿ࡾࡷࡨࡵࡰࡦࡿࠣࡪ࡮ࡾࡴࡶࡴࡨࡁࠧቲ") + str(bstack1ll11111l1l_opy_[bstack1ll111l1l1l_opy_]) + bstack111l1l_opy_ (u"ࠧࠨታ"))
            else:
                bstack1ll11111l1l_opy_[bstack1ll111l1l1l_opy_] = bstack1l1lll1llll_opy_
                self.logger.debug(bstack111l1l_opy_ (u"ࠨࡳࡢࡸࡨࡨࠥ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࡀࡿ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦࡿࠣࡷࡨࡵࡰࡦ࠿ࡾࡷࡨࡵࡰࡦࡿࠣࡪ࡮ࡾࡴࡶࡴࡨࡁࢀࡺࡥࡴࡶࡢࡪ࡮ࡾࡴࡶࡴࡨࢁࠥࡺࡲࡢࡥ࡮ࡩࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࡳ࠾ࠤቴ") + str(len(bstack1ll11111l1l_opy_)) + bstack111l1l_opy_ (u"ࠢࠣት"))
        TestFramework.bstack1llll1l111l_opy_(instance, PytestBDDFramework.bstack1l1lllll1l1_opy_, bstack1ll11111l1l_opy_)
        self.logger.debug(bstack111l1l_opy_ (u"ࠣࡵࡤࡺࡪࡪࠠࡧ࡫ࡻࡸࡺࡸࡥࡴ࠿ࡾࡰࡪࡴࠨࡵࡴࡤࡧࡰ࡫ࡤࡠࡨ࡬ࡼࡹࡻࡲࡦࡵࠬࢁࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࠣቶ") + str(instance.ref()) + bstack111l1l_opy_ (u"ࠤࠥቷ"))
        return instance
    def __1ll11111ll1_opy_(
        self,
        context: bstack1l1llll1111_opy_,
        test_framework_state: bstack1lll11l1lll_opy_,
        target: Any,
        *args,
    ):
        ctx = bstack1ll1ll11l1l_opy_.create_context(target)
        ob = bstack1lll1lll1ll_opy_(ctx, self.bstack1l1lll1l1ll_opy_, self.bstack1ll1l111lll_opy_, test_framework_state)
        TestFramework.bstack1ll111111ll_opy_(ob, {
            TestFramework.bstack1llll1111l1_opy_: context.test_framework_name,
            TestFramework.bstack1lll11l1ll1_opy_: context.test_framework_version,
            TestFramework.bstack1ll1l111ll1_opy_: [],
            PytestBDDFramework.bstack1l1lllll1l1_opy_: {},
            PytestBDDFramework.bstack1ll111ll1l1_opy_: {},
            PytestBDDFramework.bstack1ll1111l111_opy_: {},
        })
        if len(args) > 1 and isinstance(args[1], tuple):
            TestFramework.bstack1llll1l111l_opy_(ob, TestFramework.bstack1ll11llll11_opy_, str(args[1][0]))
        if context.platform_index >= 0:
            TestFramework.bstack1llll1l111l_opy_(ob, TestFramework.bstack1llll11llll_opy_, context.platform_index)
        TestFramework.bstack1lll1ll11l1_opy_[ctx.id] = ob
        self.logger.debug(bstack111l1l_opy_ (u"ࠥࡷࡦࡼࡥࡥࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࠤࡨࡺࡸ࠯࡫ࡧࡁࢀࡩࡴࡹ࠰࡬ࡨࢂࠦࡴࡢࡴࡪࡩࡹࡃࡻࡵࡣࡵ࡫ࡪࡺࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦࡩ࡯ࡵࡷࡥࡳࡩࡥࡴ࠿ࠥቸ") + str(TestFramework.bstack1lll1ll11l1_opy_.keys()) + bstack111l1l_opy_ (u"ࠦࠧቹ"))
        return ob
    @staticmethod
    def __1ll11l1l1ll_opy_(instance, args):
        request, feature, scenario = args
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack111l1l_opy_ (u"ࠬ࡯ࡤࠨቺ"): id(step),
                bstack111l1l_opy_ (u"࠭ࡴࡦࡺࡷࠫቻ"): step.name,
                bstack111l1l_opy_ (u"ࠧ࡬ࡧࡼࡻࡴࡸࡤࠨቼ"): step.keyword,
            })
        meta = {
            bstack111l1l_opy_ (u"ࠨࡨࡨࡥࡹࡻࡲࡦࠩች"): {
                bstack111l1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧቾ"): feature.name,
                bstack111l1l_opy_ (u"ࠪࡴࡦࡺࡨࠨቿ"): feature.filename,
                bstack111l1l_opy_ (u"ࠫࡩ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠩኀ"): feature.description
            },
            bstack111l1l_opy_ (u"ࠬࡹࡣࡦࡰࡤࡶ࡮ࡵࠧኁ"): {
                bstack111l1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫኂ"): scenario.name
            },
            bstack111l1l_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ኃ"): steps,
            bstack111l1l_opy_ (u"ࠨࡧࡻࡥࡲࡶ࡬ࡦࡵࠪኄ"): PytestBDDFramework.__1l1llll11ll_opy_(request.node)
        }
        instance.data.update(
            {
                TestFramework.bstack1ll111l1ll1_opy_: meta
            }
        )
    def bstack1ll1l11ll11_opy_(self, hook: Dict[str, Any]) -> None:
        bstack111l1l_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡐࡳࡱࡦࡩࡸࡹࡥࡴࠢࡷ࡬ࡪࠦࡈࡰࡱ࡮ࡐࡪࡼࡥ࡭ࠢࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࡹࠠࡴ࡫ࡰ࡭ࡱࡧࡲࠡࡶࡲࠤࡹ࡮ࡥࠡࡌࡤࡺࡦࠦࡩ࡮ࡲ࡯ࡩࡲ࡫࡮ࡵࡣࡷ࡭ࡴࡴ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡗ࡬࡮ࡹࠠ࡮ࡧࡷ࡬ࡴࡪ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡃࡩࡧࡦ࡯ࡸࠦࡴࡩࡧࠣࡌࡴࡵ࡫ࡍࡧࡹࡩࡱࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺࠢ࡬ࡲࡸ࡯ࡤࡦࠢࢁ࠳࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠳࡚ࡶ࡬ࡰࡣࡧࡩࡩࡇࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡉࡳࡷࠦࡥࡢࡥ࡫ࠤ࡫࡯࡬ࡦࠢ࡬ࡲࠥ࡮࡯ࡰ࡭ࡢࡰࡪࡼࡥ࡭ࡡࡩ࡭ࡱ࡫ࡳ࠭ࠢࡵࡩࡵࡲࡡࡤࡧࡶࠤ࡚ࠧࡥࡴࡶࡏࡩࡻ࡫࡬ࠣࠢࡺ࡭ࡹ࡮ࠠࠣࡊࡲࡳࡰࡒࡥࡷࡧ࡯ࠦࠥ࡯࡮ࠡ࡫ࡷࡷࠥࡶࡡࡵࡪ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡌࡪࠥࡧࠠࡧ࡫࡯ࡩࠥ࡯࡮ࠡࡶ࡫ࡩࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹࠡ࡯ࡤࡸࡨ࡮ࡥࡴࠢࡤࠤࡲࡵࡤࡪࡨ࡬ࡩࡩࠦࡨࡰࡱ࡮࠱ࡱ࡫ࡶࡦ࡮ࠣࡪ࡮ࡲࡥ࠭ࠢ࡬ࡸࠥࡩࡲࡦࡣࡷࡩࡸࠦࡡࠡࡎࡲ࡫ࡊࡴࡴࡳࡻࠣࡳࡧࡰࡥࡤࡶࠣࡻ࡮ࡺࡨࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࠥࡪࡥࡵࡣ࡬ࡰࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱࡙ࠥࡩ࡮࡫࡯ࡥࡷࡲࡹ࠭ࠢ࡬ࡸࠥࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠡࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵࠣࡰࡴࡩࡡࡵࡧࡧࠤ࡮ࡴࠠࡉࡱࡲ࡯ࡑ࡫ࡶࡦ࡮࠲ࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࡈࡰࡱ࡮ࡉࡻ࡫࡮ࡵࠢࡥࡽࠥࡸࡥࡱ࡮ࡤࡧ࡮ࡴࡧࠡࠤࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࠨࠠࡸ࡫ࡷ࡬ࠥࠨࡈࡰࡱ࡮ࡐࡪࡼࡥ࡭࠱ࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࡎ࡯ࡰ࡭ࡈࡺࡪࡴࡴࠣ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡖ࡫ࡩࠥࡩࡲࡦࡣࡷࡩࡩࠦࡌࡰࡩࡈࡲࡹࡸࡹࠡࡱࡥ࡮ࡪࡩࡴࡴࠢࡤࡶࡪࠦࡡࡥࡦࡨࡨࠥࡺ࡯ࠡࡶ࡫ࡩࠥ࡮࡯ࡰ࡭ࠪࡷࠥࠨ࡬ࡰࡩࡶࠦࠥࡲࡩࡴࡶ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡇࡲࡨࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࡫ࡳࡴࡱ࠺ࠡࡖ࡫ࡩࠥ࡫ࡶࡦࡰࡷࠤࡩ࡯ࡣࡵ࡫ࡲࡲࡦࡸࡹࠡࡥࡲࡲࡹࡧࡩ࡯࡫ࡱ࡫ࠥ࡫ࡸࡪࡵࡷ࡭ࡳ࡭ࠠ࡭ࡱࡪࡷࠥࡧ࡮ࡥࠢ࡫ࡳࡴࡱࠠࡪࡰࡩࡳࡷࡳࡡࡵ࡫ࡲࡲ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡭ࡵ࡯࡬ࡡ࡯ࡩࡻ࡫࡬ࡠࡨ࡬ࡰࡪࡹ࠺ࠡࡎ࡬ࡷࡹࠦ࡯ࡧࠢࡓࡥࡹ࡮ࠠࡰࡤ࡭ࡩࡨࡺࡳࠡࡨࡵࡳࡲࠦࡴࡩࡧࠣࡘࡪࡹࡴࡍࡧࡹࡩࡱࠦ࡭ࡰࡰ࡬ࡸࡴࡸࡩ࡯ࡩ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡥࡹ࡮ࡲࡤࡠ࡮ࡨࡺࡪࡲ࡟ࡧ࡫࡯ࡩࡸࡀࠠࡍ࡫ࡶࡸࠥࡵࡦࠡࡒࡤࡸ࡭ࠦ࡯ࡣ࡬ࡨࡧࡹࡹࠠࡧࡴࡲࡱࠥࡺࡨࡦࠢࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࠦ࡭ࡰࡰ࡬ࡸࡴࡸࡩ࡯ࡩ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣኅ")
        global _1ll11llll1l_opy_
        platform_index = os.environ[bstack111l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪኆ")]
        bstack1ll111l1111_opy_ = os.path.join(bstack1ll1l11lll1_opy_, (bstack1l1lll1ll1l_opy_ + str(platform_index)), bstack1l1llllll1l_opy_)
        if not os.path.exists(bstack1ll111l1111_opy_) or not os.path.isdir(bstack1ll111l1111_opy_):
            return
        logs = hook.get(bstack111l1l_opy_ (u"ࠦࡱࡵࡧࡴࠤኇ"), [])
        with os.scandir(bstack1ll111l1111_opy_) as entries:
            for entry in entries:
                abs_path = os.path.abspath(entry.path)
                if abs_path in _1ll11llll1l_opy_:
                    self.logger.info(bstack111l1l_opy_ (u"ࠧࡖࡡࡵࡪࠣࡥࡱࡸࡥࡢࡦࡼࠤࡵࡸ࡯ࡤࡧࡶࡷࡪࡪࠠࡼࡿࠥኈ").format(abs_path))
                    continue
                if entry.is_file():
                    try:
                        timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                    except Exception:
                        timestamp = bstack111l1l_opy_ (u"ࠨࠢ኉")
                    log_entry = bstack1ll111llll1_opy_(
                        kind=bstack111l1l_opy_ (u"ࠢࡕࡇࡖࡘࡤࡇࡔࡕࡃࡆࡌࡒࡋࡎࡕࠤኊ"),
                        message=bstack111l1l_opy_ (u"ࠣࠤኋ"),
                        level=bstack111l1l_opy_ (u"ࠤࠥኌ"),
                        timestamp=timestamp,
                        fileName=entry.name,
                        bstack1ll11l1l111_opy_=entry.stat().st_size,
                        bstack1ll1l1l1l11_opy_=bstack111l1l_opy_ (u"ࠥࡑࡆࡔࡕࡂࡎࡢ࡙ࡕࡒࡏࡂࡆࠥኍ"),
                        bstack1ll_opy_=os.path.abspath(entry.path),
                        bstack1l1llllllll_opy_=hook.get(TestFramework.bstack1ll11lll1l1_opy_)
                    )
                    logs.append(log_entry)
                    _1ll11llll1l_opy_.add(abs_path)
        platform_index = os.environ[bstack111l1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫ኎")]
        bstack1ll11111lll_opy_ = os.path.join(bstack1ll1l11lll1_opy_, (bstack1l1lll1ll1l_opy_ + str(platform_index)), bstack1l1llllll1l_opy_, bstack1ll11l1lll1_opy_)
        if not os.path.exists(bstack1ll11111lll_opy_) or not os.path.isdir(bstack1ll11111lll_opy_):
            self.logger.info(bstack111l1l_opy_ (u"ࠧࡔ࡯ࠡࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࡍࡵ࡯࡬ࡇࡹࡩࡳࡺࠠࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹࠡࡨࡲࡹࡳࡪࠠࡢࡶ࠽ࠤࢀࢃࠢ኏").format(bstack1ll11111lll_opy_))
        else:
            self.logger.info(bstack111l1l_opy_ (u"ࠨࡐࡳࡱࡦࡩࡸࡹࡩ࡯ࡩࠣࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࡈࡰࡱ࡮ࡉࡻ࡫࡮ࡵࠢࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࡹࠠࡧࡴࡲࡱࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹ࠻ࠢࡾࢁࠧነ").format(bstack1ll11111lll_opy_))
            with os.scandir(bstack1ll11111lll_opy_) as entries:
                for entry in entries:
                    abs_path = os.path.abspath(entry.path)
                    if abs_path in _1ll11llll1l_opy_:
                        self.logger.info(bstack111l1l_opy_ (u"ࠢࡑࡣࡷ࡬ࠥࡧ࡬ࡳࡧࡤࡨࡾࠦࡰࡳࡱࡦࡩࡸࡹࡥࡥࠢࡾࢁࠧኑ").format(abs_path))
                        continue
                    if entry.is_file():
                        try:
                            timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                        except Exception:
                            timestamp = bstack111l1l_opy_ (u"ࠣࠤኒ")
                        log_entry = bstack1ll111llll1_opy_(
                            kind=bstack111l1l_opy_ (u"ࠤࡗࡉࡘ࡚࡟ࡂࡖࡗࡅࡈࡎࡍࡆࡐࡗࠦና"),
                            message=bstack111l1l_opy_ (u"ࠥࠦኔ"),
                            level=bstack111l1l_opy_ (u"ࠦࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࠣን"),
                            timestamp=timestamp,
                            fileName=entry.name,
                            bstack1ll11l1l111_opy_=entry.stat().st_size,
                            bstack1ll1l1l1l11_opy_=bstack111l1l_opy_ (u"ࠧࡓࡁࡏࡗࡄࡐࡤ࡛ࡐࡍࡑࡄࡈࠧኖ"),
                            bstack1ll_opy_=os.path.abspath(entry.path),
                            bstack1ll1l1l1ll1_opy_=hook.get(TestFramework.bstack1ll11lll1l1_opy_)
                        )
                        logs.append(log_entry)
                        _1ll11llll1l_opy_.add(abs_path)
        hook[bstack111l1l_opy_ (u"ࠨ࡬ࡰࡩࡶࠦኗ")] = logs
    def bstack1ll11llllll_opy_(
        self,
        bstack1ll11ll11l1_opy_: bstack1lll1lll1ll_opy_,
        entries: List[bstack1ll111llll1_opy_],
    ):
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = os.environ.get(bstack111l1l_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡍࡋࡢࡆࡎࡔ࡟ࡔࡇࡖࡗࡎࡕࡎࡠࡋࡇࠦኘ"))
        req.platform_index = TestFramework.get_state(bstack1ll11ll11l1_opy_, TestFramework.bstack1llll11llll_opy_)
        req.execution_context.hash = str(bstack1ll11ll11l1_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll11ll11l1_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll11ll11l1_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1ll11ll11l1_opy_, TestFramework.bstack1llll1111l1_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1ll11ll11l1_opy_, TestFramework.bstack1lll11l1ll1_opy_)
            log_entry.uuid = entry.bstack1l1llllllll_opy_ if entry.bstack1l1llllllll_opy_ else TestFramework.get_state(bstack1ll11ll11l1_opy_, TestFramework.bstack1lll1ll1lll_opy_)
            log_entry.test_framework_state = bstack1ll11ll11l1_opy_.state.name
            log_entry.message = entry.message.encode(bstack111l1l_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢኙ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            if isinstance(entry.level, str) and len(entry.level.strip()) > 0:
                log_entry.level = entry.level.strip()
            if entry.kind == bstack111l1l_opy_ (u"ࠤࡗࡉࡘ࡚࡟ࡂࡖࡗࡅࡈࡎࡍࡆࡐࡗࠦኚ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1ll11l1l111_opy_
                log_entry.file_path = entry.bstack1ll_opy_
        def bstack1ll111lll1l_opy_():
            bstack1l1ll111ll_opy_ = datetime.now()
            try:
                self.bstack1llll11ll11_opy_.LogCreatedEvent(req)
                bstack1ll11ll11l1_opy_.bstack1l1l111ll1_opy_(bstack111l1l_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡵࡨࡲࡩࡥ࡬ࡰࡩࡢࡧࡷ࡫ࡡࡵࡧࡧࡣࡪࡼࡥ࡯ࡶࡢࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࠢኛ"), datetime.now() - bstack1l1ll111ll_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack111l1l_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࡵࡨࡲࡩࡥ࡬ࡰࡩࡢࡧࡷ࡫ࡡࡵࡧࡧࡣࡪࡼࡥ࡯ࡶࡢࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࠠࡼࡿࠥኜ").format(str(e)))
                traceback.print_exc()
        self.bstack1lll11l1l11_opy_.enqueue(bstack1ll111lll1l_opy_)
    def __1ll1l1111l1_opy_(self, instance) -> None:
        bstack111l1l_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡏࡳࡦࡪࡳࠡࡥࡸࡷࡹࡵ࡭ࠡࡶࡤ࡫ࡸࠦࡦࡰࡴࠣࡸ࡭࡫ࠠࡨ࡫ࡹࡩࡳࠦࡴࡦࡵࡷࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡈࡸࡥࡢࡶࡨࡷࠥࡧࠠࡥ࡫ࡦࡸࠥࡩ࡯࡯ࡶࡤ࡭ࡳ࡯࡮ࡨࠢࡷࡩࡸࡺࠠ࡭ࡧࡹࡩࡱࠦࡣࡶࡵࡷࡳࡲࠦ࡭ࡦࡶࡤࡨࡦࡺࡡࠡࡴࡨࡸࡷ࡯ࡥࡷࡧࡧࠤ࡫ࡸ࡯࡮ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡇࡺࡹࡴࡰ࡯ࡗࡥ࡬ࡓࡡ࡯ࡣࡪࡩࡷࠦࡡ࡯ࡦࠣࡹࡵࡪࡡࡵࡧࡶࠤࡹ࡮ࡥࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࠣࡷࡹࡧࡴࡦࠢࡸࡷ࡮ࡴࡧࠡࡵࡨࡸࡤࡹࡴࡢࡶࡨࡣࡪࡴࡴࡳ࡫ࡨࡷ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥኝ")
        bstack1l1llll1l1l_opy_ = {bstack111l1l_opy_ (u"ࠨࡣࡶࡵࡷࡳࡲࡥ࡭ࡦࡶࡤࡨࡦࡺࡡࠣኞ"): bstack1ll11l1llll_opy_.bstack1ll1l1l11l1_opy_()}
        TestFramework.bstack1ll111111ll_opy_(instance, bstack1l1llll1l1l_opy_)
    @staticmethod
    def __1ll1l1l1111_opy_(instance, args):
        request, bstack1ll111l11ll_opy_ = args
        bstack1ll1111l1l1_opy_ = id(bstack1ll111l11ll_opy_)
        bstack1ll111ll1ll_opy_ = instance.data[TestFramework.bstack1ll111l1ll1_opy_]
        step = next(filter(lambda st: st[bstack111l1l_opy_ (u"ࠧࡪࡦࠪኟ")] == bstack1ll1111l1l1_opy_, bstack1ll111ll1ll_opy_[bstack111l1l_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧአ")]), None)
        step.update({
            bstack111l1l_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭ኡ"): datetime.now(tz=timezone.utc)
        })
        index = next((i for i, st in enumerate(bstack1ll111ll1ll_opy_[bstack111l1l_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩኢ")]) if st[bstack111l1l_opy_ (u"ࠫ࡮ࡪࠧኣ")] == step[bstack111l1l_opy_ (u"ࠬ࡯ࡤࠨኤ")]), None)
        if index is not None:
            bstack1ll111ll1ll_opy_[bstack111l1l_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬእ")][index] = step
        instance.data[TestFramework.bstack1ll111l1ll1_opy_] = bstack1ll111ll1ll_opy_
    @staticmethod
    def __1ll111lll11_opy_(instance, args):
        bstack111l1l_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡼ࡮ࡥ࡯ࠢ࡯ࡩࡳࠦࡡࡳࡩࡶࠤ࡮ࡹࠠ࠳࠮ࠣ࡭ࡹࠦࡳࡪࡩࡱ࡭࡫࡯ࡥࡴࠢࡷ࡬ࡪࡸࡥࠡ࡫ࡶࠤࡳࡵࠠࡦࡺࡦࡩࡵࡺࡩࡰࡰࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡣࡵ࡫ࡸࠦࡡࡳࡧࠣ࠱ࠥࡡࡲࡦࡳࡸࡩࡸࡺࠬࠡࡵࡷࡩࡵࡣࠊࠡࠢࠣࠤࠥࠦࠠࠡ࡫ࡩࠤࡦࡸࡧࡴࠢࡤࡶࡪࠦ࠳ࠡࡶ࡫ࡩࡳࠦࡴࡩࡧࠣࡰࡦࡹࡴࠡࡸࡤࡰࡺ࡫ࠠࡪࡵࠣࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥኦ")
        bstack1ll11l1ll11_opy_ = datetime.now(tz=timezone.utc)
        request = args[0]
        bstack1ll111l11ll_opy_ = args[1]
        bstack1ll1111l1l1_opy_ = id(bstack1ll111l11ll_opy_)
        bstack1ll111ll1ll_opy_ = instance.data[TestFramework.bstack1ll111l1ll1_opy_]
        step = None
        if bstack1ll1111l1l1_opy_ is not None and bstack1ll111ll1ll_opy_.get(bstack111l1l_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧኧ")):
            step = next(filter(lambda st: st[bstack111l1l_opy_ (u"ࠩ࡬ࡨࠬከ")] == bstack1ll1111l1l1_opy_, bstack1ll111ll1ll_opy_[bstack111l1l_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩኩ")]), None)
            step.update({
                bstack111l1l_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩኪ"): bstack1ll11l1ll11_opy_,
            })
        if len(args) > 2:
            exception = args[2]
            step.update({
                bstack111l1l_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬካ"): bstack111l1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ኬ"),
                bstack111l1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨክ"): str(exception)
            })
        else:
            if step is not None:
                step.update({
                    bstack111l1l_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨኮ"): bstack111l1l_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩኯ"),
                })
        index = next((i for i, st in enumerate(bstack1ll111ll1ll_opy_[bstack111l1l_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩኰ")]) if st[bstack111l1l_opy_ (u"ࠫ࡮ࡪࠧ኱")] == step[bstack111l1l_opy_ (u"ࠬ࡯ࡤࠨኲ")]), None)
        if index is not None:
            bstack1ll111ll1ll_opy_[bstack111l1l_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬኳ")][index] = step
        instance.data[TestFramework.bstack1ll111l1ll1_opy_] = bstack1ll111ll1ll_opy_
    @staticmethod
    def __1l1llll11ll_opy_(node):
        try:
            examples = []
            if hasattr(node, bstack111l1l_opy_ (u"ࠧࡤࡣ࡯ࡰࡸࡶࡥࡤࠩኴ")):
                examples = list(node.callspec.params[bstack111l1l_opy_ (u"ࠨࡡࡳࡽࡹ࡫ࡳࡵࡡࡥࡨࡩࡥࡥࡹࡣࡰࡴࡱ࡫ࠧኵ")].values())
            return examples
        except:
            return []
    def bstack1ll11l1l1l1_opy_(self, instance: bstack1lll1lll1ll_opy_, bstack1llll1l11l1_opy_: Tuple[bstack1lll11l1lll_opy_, bstack1llll111111_opy_]):
        bstack1ll11l1111l_opy_ = (
            PytestBDDFramework.bstack1ll1l111l1l_opy_
            if bstack1llll1l11l1_opy_[1] == bstack1llll111111_opy_.PRE
            else PytestBDDFramework.bstack1ll111l1l11_opy_
        )
        hook = PytestBDDFramework.bstack1l1lll1lll1_opy_(instance, bstack1ll11l1111l_opy_)
        entries = hook.get(TestFramework.bstack1ll1l1l111l_opy_, []) if isinstance(hook, dict) else []
        entries.extend(TestFramework.get_state(instance, TestFramework.bstack1ll1l111ll1_opy_, []))
        return entries
    def bstack1ll111lllll_opy_(self, instance: bstack1lll1lll1ll_opy_, bstack1llll1l11l1_opy_: Tuple[bstack1lll11l1lll_opy_, bstack1llll111111_opy_]):
        bstack1ll11l1111l_opy_ = (
            PytestBDDFramework.bstack1ll1l111l1l_opy_
            if bstack1llll1l11l1_opy_[1] == bstack1llll111111_opy_.PRE
            else PytestBDDFramework.bstack1ll111l1l11_opy_
        )
        PytestBDDFramework.bstack1l1llllll11_opy_(instance, bstack1ll11l1111l_opy_)
        TestFramework.get_state(instance, TestFramework.bstack1ll1l111ll1_opy_, []).clear()
    @staticmethod
    def bstack1l1lll1lll1_opy_(instance: bstack1lll1lll1ll_opy_, bstack1ll11l1111l_opy_: str):
        bstack1ll11l11l11_opy_ = (
            PytestBDDFramework.bstack1ll111ll1l1_opy_
            if bstack1ll11l1111l_opy_ == PytestBDDFramework.bstack1ll111l1l11_opy_
            else PytestBDDFramework.bstack1ll1111l111_opy_
        )
        bstack1l1lllll1ll_opy_ = TestFramework.get_state(instance, bstack1ll11l1111l_opy_, None)
        bstack1ll1111lll1_opy_ = TestFramework.get_state(instance, bstack1ll11l11l11_opy_, None) if bstack1l1lllll1ll_opy_ else None
        return (
            bstack1ll1111lll1_opy_[bstack1l1lllll1ll_opy_][-1]
            if isinstance(bstack1ll1111lll1_opy_, dict) and len(bstack1ll1111lll1_opy_.get(bstack1l1lllll1ll_opy_, [])) > 0
            else None
        )
    @staticmethod
    def bstack1l1llllll11_opy_(instance: bstack1lll1lll1ll_opy_, bstack1ll11l1111l_opy_: str):
        hook = PytestBDDFramework.bstack1l1lll1lll1_opy_(instance, bstack1ll11l1111l_opy_)
        if isinstance(hook, dict):
            hook.get(TestFramework.bstack1ll1l1l111l_opy_, []).clear()
    @staticmethod
    def __1l1llll1lll_opy_(instance: bstack1lll1lll1ll_opy_, *args):
        if len(args) < 2 or not callable(getattr(args[1], bstack111l1l_opy_ (u"ࠤࡪࡩࡹࡥࡲࡦࡥࡲࡶࡩࡹࠢ኶"), None)):
            return
        if os.getenv(bstack111l1l_opy_ (u"ࠥࡗࡉࡑ࡟ࡄࡎࡌࡣࡋࡒࡁࡈࡡࡏࡓࡌ࡙ࠢ኷"), bstack111l1l_opy_ (u"ࠦ࠶ࠨኸ")) != bstack111l1l_opy_ (u"ࠧ࠷ࠢኹ"):
            PytestBDDFramework.logger.warning(bstack111l1l_opy_ (u"ࠨࡩࡨࡰࡲࡶ࡮ࡴࡧࠡࡥࡤࡴࡱࡵࡧࠣኺ"))
            return
        bstack1ll1l11l1l1_opy_ = {
            bstack111l1l_opy_ (u"ࠢࡴࡧࡷࡹࡵࠨኻ"): (PytestBDDFramework.bstack1ll1l111l1l_opy_, PytestBDDFramework.bstack1ll1111l111_opy_),
            bstack111l1l_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࠥኼ"): (PytestBDDFramework.bstack1ll111l1l11_opy_, PytestBDDFramework.bstack1ll111ll1l1_opy_),
        }
        for when in (bstack111l1l_opy_ (u"ࠤࡶࡩࡹࡻࡰࠣኽ"), bstack111l1l_opy_ (u"ࠥࡧࡦࡲ࡬ࠣኾ"), bstack111l1l_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࠨ኿")):
            bstack1ll1l11111l_opy_ = args[1].get_records(when)
            if not bstack1ll1l11111l_opy_:
                continue
            records = [
                bstack1ll111llll1_opy_(
                    kind=TestFramework.bstack1l1lllllll1_opy_,
                    message=r.message,
                    level=r.levelname if hasattr(r, bstack111l1l_opy_ (u"ࠧࡲࡥࡷࡧ࡯ࡲࡦࡳࡥࠣዀ")) and r.levelname else None,
                    timestamp=(
                        datetime.fromtimestamp(r.created, tz=timezone.utc)
                        if hasattr(r, bstack111l1l_opy_ (u"ࠨࡣࡳࡧࡤࡸࡪࡪࠢ዁")) and r.created
                        else None
                    ),
                )
                for r in bstack1ll1l11111l_opy_
                if isinstance(getattr(r, bstack111l1l_opy_ (u"ࠢ࡮ࡧࡶࡷࡦ࡭ࡥࠣዂ"), None), str) and r.message.strip()
            ]
            if not records:
                continue
            bstack1ll11ll1111_opy_, bstack1ll11l11l11_opy_ = bstack1ll1l11l1l1_opy_.get(when, (None, None))
            bstack1ll1l1l11ll_opy_ = TestFramework.get_state(instance, bstack1ll11ll1111_opy_, None) if bstack1ll11ll1111_opy_ else None
            bstack1ll1111lll1_opy_ = TestFramework.get_state(instance, bstack1ll11l11l11_opy_, None) if bstack1ll1l1l11ll_opy_ else None
            if isinstance(bstack1ll1111lll1_opy_, dict) and len(bstack1ll1111lll1_opy_.get(bstack1ll1l1l11ll_opy_, [])) > 0:
                hook = bstack1ll1111lll1_opy_[bstack1ll1l1l11ll_opy_][-1]
                if isinstance(hook, dict) and TestFramework.bstack1ll1l1l111l_opy_ in hook:
                    hook[TestFramework.bstack1ll1l1l111l_opy_].extend(records)
                    continue
            logs = TestFramework.get_state(instance, TestFramework.bstack1ll1l111ll1_opy_, [])
            logs.extend(records)
    @staticmethod
    def __1ll1111llll_opy_(args) -> Dict[str, Any]:
        request, feature, scenario = args
        test_id = request.node.nodeid
        test_name = PytestBDDFramework.__1ll1111ll11_opy_(request.node, scenario)
        bstack1ll1l11ll1l_opy_ = feature.filename
        if not test_id or not test_name or not bstack1ll1l11ll1l_opy_:
            return None
        code = None
        return {
            TestFramework.bstack1lll1ll1lll_opy_: uuid4().__str__(),
            TestFramework.bstack1l1lll1l1l1_opy_: test_id,
            TestFramework.bstack1ll1l1111ll_opy_: test_name,
            TestFramework.bstack1ll11ll111l_opy_: test_id,
            TestFramework.bstack1ll11l1ll1l_opy_: bstack1ll1l11ll1l_opy_,
            TestFramework.bstack1ll1111111l_opy_: PytestBDDFramework.__1ll11111l11_opy_(feature, scenario),
            TestFramework.bstack1ll1111l11l_opy_: code,
            TestFramework.bstack1lll1ll1l1l_opy_: TestFramework.bstack1ll1l11l111_opy_,
            TestFramework.bstack1lll1111l11_opy_: test_name
        }
    @staticmethod
    def __1ll1111ll11_opy_(node, scenario):
        if hasattr(node, bstack111l1l_opy_ (u"ࠨࡥࡤࡰࡱࡹࡰࡦࡥࠪዃ")):
            parts = node.nodeid.rsplit(bstack111l1l_opy_ (u"ࠤ࡞ࠦዄ"))
            params = parts[-1]
            return bstack111l1l_opy_ (u"ࠥࡿࢂ࡛ࠦࡼࡿࠥዅ").format(scenario.name, params)
        return scenario.name
    @staticmethod
    def __1ll11111l11_opy_(feature, scenario) -> List[str]:
        return (list(feature.tags) if hasattr(feature, bstack111l1l_opy_ (u"ࠫࡹࡧࡧࡴࠩ዆")) else []) + (list(scenario.tags) if hasattr(scenario, bstack111l1l_opy_ (u"ࠬࡺࡡࡨࡵࠪ዇")) else [])
    @staticmethod
    def __1l1lll1ll11_opy_(location):
        return bstack111l1l_opy_ (u"ࠨ࠺࠻ࠤወ").join(filter(lambda x: isinstance(x, str), location))