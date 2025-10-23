# coding: UTF-8
import sys
bstack111lll1_opy_ = sys.version_info [0] == 2
bstack11l1l1_opy_ = 2048
bstack11lllll_opy_ = 7
def bstack11lll1_opy_ (bstack111lll_opy_):
    global bstack11ll1l_opy_
    bstack11l11l1_opy_ = ord (bstack111lll_opy_ [-1])
    bstack1l1l_opy_ = bstack111lll_opy_ [:-1]
    bstack1l11l1_opy_ = bstack11l11l1_opy_ % len (bstack1l1l_opy_)
    bstack1lll1l_opy_ = bstack1l1l_opy_ [:bstack1l11l1_opy_] + bstack1l1l_opy_ [bstack1l11l1_opy_:]
    if bstack111lll1_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    return eval (bstack1111lll_opy_)
import os
from datetime import datetime, timezone
from uuid import uuid4
from typing import Dict, List, Any, Tuple
from browserstack_sdk.sdk_cli.bstack1ll1lllll11_opy_ import bstack1ll1ll11l1l_opy_
from browserstack_sdk.sdk_cli.utils.bstack111ll1lll1_opy_ import bstack1ll11llllll_opy_
from pathlib import Path
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.test_framework import (
    TestFramework,
    bstack1lll1l1ll11_opy_,
    bstack1llll11111l_opy_,
    bstack1llll11l111_opy_,
    bstack1ll111l11ll_opy_,
    bstack1l1lllll111_opy_,
)
import traceback
from bstack_utils.helper import bstack1ll111ll1l1_opy_
from bstack_utils.bstack1111l111l1_opy_ import bstack1lllllll111_opy_
from bstack_utils.constants import EVENTS
from browserstack_sdk.sdk_cli.utils.bstack1ll111l1111_opy_ import bstack1ll1111l111_opy_
from browserstack_sdk.sdk_cli.bstack1lll11l1l1l_opy_ import bstack1lll11l11ll_opy_
bstack1ll11lll11l_opy_ = bstack1ll111ll1l1_opy_()
bstack1ll1111l1ll_opy_ = bstack11lll1_opy_ (u"ࠤࡘࡴࡱࡵࡡࡥࡧࡧࡅࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳ࠮ࠤሕ")
bstack1ll11l11lll_opy_ = bstack11lll1_opy_ (u"ࠥࡌࡴࡵ࡫ࡍࡧࡹࡩࡱࠨሖ")
bstack1ll111ll1ll_opy_ = bstack11lll1_opy_ (u"ࠦࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࡉࡱࡲ࡯ࡊࡼࡥ࡯ࡶࠥሗ")
bstack1l1llll1l11_opy_ = 1.0
_1ll1l1111l1_opy_ = set()
class PytestBDDFramework(TestFramework):
    bstack1ll11ll1lll_opy_ = bstack11lll1_opy_ (u"ࠧࡺࡥࡴࡶࡢࡪ࡮ࡾࡴࡶࡴࡨࡷࠧመ")
    bstack1l1llll1ll1_opy_ = bstack11lll1_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡵࡢࡷࡹࡧࡲࡵࡧࡧࠦሙ")
    bstack1l1llll11l1_opy_ = bstack11lll1_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡶࡣ࡫࡯࡮ࡪࡵ࡫ࡩࡩࠨሚ")
    bstack1ll11111lll_opy_ = bstack11lll1_opy_ (u"ࠣࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡱࡧࡳࡵࡡࡶࡸࡦࡸࡴࡦࡦࠥማ")
    bstack1ll11ll1l1l_opy_ = bstack11lll1_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡲࡡࡴࡶࡢࡪ࡮ࡴࡩࡴࡪࡨࡨࠧሜ")
    bstack1l1lll1lll1_opy_: bool
    bstack1lll11l1l1l_opy_: bstack1lll11l11ll_opy_  = None
    bstack1l1llll1lll_opy_ = [
        bstack1lll1l1ll11_opy_.BEFORE_ALL,
        bstack1lll1l1ll11_opy_.AFTER_ALL,
        bstack1lll1l1ll11_opy_.BEFORE_EACH,
        bstack1lll1l1ll11_opy_.AFTER_EACH,
    ]
    def __init__(
        self,
        bstack1ll1l111ll1_opy_: Dict[str, str],
        bstack1ll1l1l11ll_opy_: List[str]=[bstack11lll1_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠢም")],
        bstack1lll11l1l1l_opy_: bstack1lll11l11ll_opy_ = None,
        bstack1llll11lll1_opy_=None
    ):
        super().__init__(bstack1ll1l1l11ll_opy_, bstack1ll1l111ll1_opy_, bstack1lll11l1l1l_opy_)
        self.bstack1l1lll1lll1_opy_ = any(bstack11lll1_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠣሞ") in item.lower() for item in bstack1ll1l1l11ll_opy_)
        self.bstack1llll11lll1_opy_ = bstack1llll11lll1_opy_
    def track_event(
        self,
        context: bstack1ll111l11ll_opy_,
        test_framework_state: bstack1lll1l1ll11_opy_,
        test_hook_state: bstack1llll11l111_opy_,
        *args,
        **kwargs,
    ):
        super().track_event(self, context, test_framework_state, test_hook_state, *args, **kwargs)
        if test_framework_state == bstack1lll1l1ll11_opy_.TEST or test_framework_state in PytestBDDFramework.bstack1l1llll1lll_opy_:
            bstack1ll11llllll_opy_(test_framework_state, test_hook_state)
        if test_framework_state == bstack1lll1l1ll11_opy_.NONE:
            self.logger.warning(bstack11lll1_opy_ (u"ࠧ࡯ࡧ࡯ࡱࡵࡩࡩࠦࡣࡢ࡮࡯ࡦࡦࡩ࡫ࠡࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿࠣࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࡂࠨሟ") + str(test_hook_state) + bstack11lll1_opy_ (u"ࠨࠢሠ"))
            return
        if not self.bstack1l1lll1lll1_opy_:
            self.logger.warning(bstack11lll1_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡥࡷࡧࡱࡸ࠿ࠦࡵ࡯ࡵࡸࡴࡵࡵࡲࡵࡧࡧࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࠽ࠣሡ") + str(str(self.bstack1ll1l1l11ll_opy_)) + bstack11lll1_opy_ (u"ࠣࠤሢ"))
            return
        if not isinstance(args, tuple) or len(args) == 0:
            self.logger.warning(bstack11lll1_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡧࡹࡩࡳࡺ࠺ࠡࡷࡱࡩࡽࡶࡥࡤࡶࡨࡨࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦሣ") + str(kwargs) + bstack11lll1_opy_ (u"ࠥࠦሤ"))
            return
        instance = self.__1ll1111l11l_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        if not instance:
            self.logger.debug(bstack11lll1_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡹࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࡼࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࢀࠤࡦࡸࡧࡴ࠿ࠥሥ") + str(args) + bstack11lll1_opy_ (u"ࠧࠨሦ"))
            return
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1l1llll1lll_opy_ and test_hook_state == bstack1llll11l111_opy_.PRE:
                bstack1ll1l1111ll_opy_ = bstack1lllllll111_opy_.bstack1ll11111l1l_opy_(EVENTS.bstack1ll1ll1l11_opy_.value)
                name = str(EVENTS.bstack1ll1ll1l11_opy_.name)+bstack11lll1_opy_ (u"ࠨ࠺ࠣሧ")+str(test_framework_state.name)
                TestFramework.bstack1ll111l1lll_opy_(instance, name, bstack1ll1l1111ll_opy_)
        except Exception as e:
            self.logger.debug(bstack11lll1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡨࡰࡱ࡮ࠤࡪࡸࡲࡰࡴࠣࡴࡷ࡫࠺ࠡࡽࢀࠦረ").format(e))
        try:
            if test_framework_state == bstack1lll1l1ll11_opy_.TEST:
                if not TestFramework.bstack1llll1l11l1_opy_(instance, TestFramework.bstack1ll11llll1l_opy_) and test_hook_state == bstack1llll11l111_opy_.PRE:
                    if not (len(args) >= 3):
                        return
                    test = PytestBDDFramework.__1ll1l11l1l1_opy_(args)
                    if test:
                        instance.data.update(test)
                        self.logger.debug(bstack11lll1_opy_ (u"ࠣ࡮ࡲࡥࡩ࡫ࡤࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࡿ࡮ࡴࡳࡵࡣࡱࡧࡪ࠴ࡲࡦࡨࠫ࠭ࢂࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࠣሩ") + str(test_hook_state) + bstack11lll1_opy_ (u"ࠤࠥሪ"))
                if test_hook_state == bstack1llll11l111_opy_.PRE and not TestFramework.bstack1llll1l11l1_opy_(instance, TestFramework.bstack1ll1l111l1l_opy_):
                    TestFramework.bstack1lllll11l11_opy_(instance, TestFramework.bstack1ll1l111l1l_opy_, datetime.now(tz=timezone.utc))
                    PytestBDDFramework.__1ll11ll1ll1_opy_(instance, args)
                    self.logger.debug(bstack11lll1_opy_ (u"ࠥࡷࡪࡺࠠࡵࡧࡶࡸ࠲ࡹࡴࡢࡴࡷࠤ࡫ࡵࡲࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࡿ࡮ࡴࡳࡵࡣࡱࡧࡪ࠴ࡲࡦࡨࠫ࠭ࢂࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࠣራ") + str(test_hook_state) + bstack11lll1_opy_ (u"ࠦࠧሬ"))
                elif test_hook_state == bstack1llll11l111_opy_.POST and not TestFramework.bstack1llll1l11l1_opy_(instance, TestFramework.bstack1ll1l1l1ll1_opy_):
                    TestFramework.bstack1lllll11l11_opy_(instance, TestFramework.bstack1ll1l1l1ll1_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack11lll1_opy_ (u"ࠧࡹࡥࡵࠢࡷࡩࡸࡺ࠭ࡦࡰࡧࠤ࡫ࡵࡲࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࡿ࡮ࡴࡳࡵࡣࡱࡧࡪ࠴ࡲࡦࡨࠫ࠭ࢂࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࠣር") + str(test_hook_state) + bstack11lll1_opy_ (u"ࠨࠢሮ"))
            elif test_framework_state == bstack1lll1l1ll11_opy_.STEP:
                if test_hook_state == bstack1llll11l111_opy_.PRE:
                    PytestBDDFramework.__1ll1l1l11l1_opy_(instance, args)
                elif test_hook_state == bstack1llll11l111_opy_.POST:
                    PytestBDDFramework.__1ll11ll1111_opy_(instance, args)
            elif test_framework_state == bstack1lll1l1ll11_opy_.LOG and test_hook_state == bstack1llll11l111_opy_.POST:
                PytestBDDFramework.__1ll11lll111_opy_(instance, *args)
            elif test_framework_state == bstack1lll1l1ll11_opy_.LOG_REPORT and test_hook_state == bstack1llll11l111_opy_.POST:
                self.__1ll11111l11_opy_(instance, *args)
                self.__1ll11lllll1_opy_(instance)
            elif test_framework_state in PytestBDDFramework.bstack1l1llll1lll_opy_:
                self.__1ll1l1ll11l_opy_(instance, test_framework_state, test_hook_state, *args)
            self.logger.debug(bstack11lll1_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡥࡷࡧࡱࡸ࠿ࠦࡨࡢࡰࡧࡰࡪࡪࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࡽࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࢁࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࠣሯ") + str(instance.ref()) + bstack11lll1_opy_ (u"ࠣࠤሰ"))
        except Exception as e:
            self.logger.error(e)
            traceback.print_exc()
        self.bstack1ll1111lll1_opy_(instance, (test_framework_state, test_hook_state), *args, **kwargs)
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1l1llll1lll_opy_ and test_hook_state == bstack1llll11l111_opy_.POST:
                name = str(EVENTS.bstack1ll1ll1l11_opy_.name)+bstack11lll1_opy_ (u"ࠤ࠽ࠦሱ")+str(test_framework_state.name)
                bstack1ll1l1111ll_opy_ = TestFramework.bstack1ll111l1ll1_opy_(instance, name)
                bstack1lllllll111_opy_.end(EVENTS.bstack1ll1ll1l11_opy_.value, bstack1ll1l1111ll_opy_+bstack11lll1_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥሲ"), bstack1ll1l1111ll_opy_+bstack11lll1_opy_ (u"ࠦ࠿࡫࡮ࡥࠤሳ"), True, None, test_framework_state.name)
        except Exception as e:
            self.logger.debug(bstack11lll1_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡭ࡵ࡯࡬ࠢࡨࡶࡷࡵࡲ࠻ࠢࡾࢁࠧሴ").format(e))
    def bstack1ll11lll1l1_opy_(self):
        return self.bstack1l1lll1lll1_opy_
    def __1ll1l11ll1l_opy_(self, *args):
        if len(args) > 2 and callable(getattr(args[2], bstack11lll1_opy_ (u"ࠨࡧࡦࡶࡢࡶࡪࡹࡵ࡭ࡶࠥስ"), None)):
            rep = args[2].get_result()
            if rep:
                return TestFramework.bstack1ll1l11l11l_opy_(rep, [bstack11lll1_opy_ (u"ࠢࡸࡪࡨࡲࠧሶ"), bstack11lll1_opy_ (u"ࠣࡱࡸࡸࡨࡵ࡭ࡦࠤሷ"), bstack11lll1_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤሸ"), bstack11lll1_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥሹ"), bstack11lll1_opy_ (u"ࠦࡸࡱࡩࡱࡲࡨࡨࠧሺ"), bstack11lll1_opy_ (u"ࠧࡲ࡯࡯ࡩࡵࡩࡵࡸࡴࡦࡺࡷࠦሻ")])
        return None
    def __1ll11111l11_opy_(self, instance: bstack1llll11111l_opy_, *args):
        result = self.__1ll1l11ll1l_opy_(*args)
        if not result:
            return
        failure = None
        bstack1111111l1l_opy_ = None
        if result.get(bstack11lll1_opy_ (u"ࠨ࡯ࡶࡶࡦࡳࡲ࡫ࠢሼ"), None) == bstack11lll1_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢሽ") and len(args) > 1 and getattr(args[1], bstack11lll1_opy_ (u"ࠣࡧࡻࡧ࡮ࡴࡦࡰࠤሾ"), None) is not None:
            failure = [{bstack11lll1_opy_ (u"ࠩࡥࡥࡨࡱࡴࡳࡣࡦࡩࠬሿ"): [args[1].excinfo.exconly(), result.get(bstack11lll1_opy_ (u"ࠥࡰࡴࡴࡧࡳࡧࡳࡶࡹ࡫ࡸࡵࠤቀ"), None)]}]
            bstack1111111l1l_opy_ = bstack11lll1_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࡅࡳࡴࡲࡶࠧቁ") if bstack11lll1_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࠣቂ") in getattr(args[1].excinfo, bstack11lll1_opy_ (u"ࠨࡴࡺࡲࡨࡲࡦࡳࡥࠣቃ"), bstack11lll1_opy_ (u"ࠢࠣቄ")) else bstack11lll1_opy_ (u"ࠣࡗࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳࠤቅ")
        bstack1l1lll1ll1l_opy_ = result.get(bstack11lll1_opy_ (u"ࠤࡲࡹࡹࡩ࡯࡮ࡧࠥቆ"), TestFramework.bstack1ll111l1l11_opy_)
        if bstack1l1lll1ll1l_opy_ != TestFramework.bstack1ll111l1l11_opy_:
            TestFramework.bstack1lllll11l11_opy_(instance, TestFramework.bstack1l1llllll11_opy_, datetime.now(tz=timezone.utc))
        TestFramework.bstack1ll1l11lll1_opy_(instance, {
            TestFramework.bstack1lll1l1lll1_opy_: failure,
            TestFramework.bstack1l1llll11ll_opy_: bstack1111111l1l_opy_,
            TestFramework.bstack1lll1ll111l_opy_: bstack1l1lll1ll1l_opy_,
        })
    def __1ll1111l11l_opy_(
        self,
        context: bstack1ll111l11ll_opy_,
        test_framework_state: bstack1lll1l1ll11_opy_,
        test_hook_state: bstack1llll11l111_opy_,
        *args,
        **kwargs,
    ):
        instance = None
        if test_framework_state == bstack1lll1l1ll11_opy_.SETUP_FIXTURE:
            instance = self.__1ll111llll1_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        else:
            target = None # bstack1ll11ll11ll_opy_ bstack1l1lllll1ll_opy_ this to be bstack11lll1_opy_ (u"ࠥࡲࡴࡪࡥࡪࡦࠥቇ")
            if test_framework_state == bstack1lll1l1ll11_opy_.INIT_TEST:
                target = args[0] if isinstance(args[0], str) else None
                if target:
                    self.__1ll111lllll_opy_(context, test_framework_state, target, *args)
            elif test_framework_state == bstack1lll1l1ll11_opy_.LOG:
                nodeid = getattr(getattr(args[0], bstack11lll1_opy_ (u"ࠦࡳࡵࡤࡦࠤቈ"), None), bstack11lll1_opy_ (u"ࠧࡴ࡯ࡥࡧ࡬ࡨࠧ቉"), None) if args else None
                if isinstance(nodeid, str):
                    target = nodeid
            elif getattr(args[0], bstack11lll1_opy_ (u"ࠨ࡮ࡰࡦࡨࠦቊ"), None):
                target = args[0].node.nodeid
            elif getattr(args[0], bstack11lll1_opy_ (u"ࠢ࡯ࡱࡧࡩ࡮ࡪࠢቋ"), None):
                target = args[0].nodeid
            instance = TestFramework.bstack1ll111l111l_opy_(target) if target else None
        return instance
    def __1ll1l1ll11l_opy_(
        self,
        instance: bstack1llll11111l_opy_,
        test_framework_state: bstack1lll1l1ll11_opy_,
        test_hook_state: bstack1llll11l111_opy_,
        *args,
    ):
        key = test_framework_state.name
        bstack1l1lll1ll11_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1l1llll1ll1_opy_, {})
        if not key in bstack1l1lll1ll11_opy_:
            bstack1l1lll1ll11_opy_[key] = []
        bstack1ll1111ll11_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1l1llll11l1_opy_, {})
        if not key in bstack1ll1111ll11_opy_:
            bstack1ll1111ll11_opy_[key] = []
        bstack1ll11l11ll1_opy_ = {
            PytestBDDFramework.bstack1l1llll1ll1_opy_: bstack1l1lll1ll11_opy_,
            PytestBDDFramework.bstack1l1llll11l1_opy_: bstack1ll1111ll11_opy_,
        }
        if test_hook_state == bstack1llll11l111_opy_.PRE:
            hook_name = args[1] if len(args) > 1 else None
            hook = {
                bstack11lll1_opy_ (u"ࠣ࡭ࡨࡽࠧቌ"): key,
                TestFramework.bstack1ll11l1llll_opy_: uuid4().__str__(),
                TestFramework.bstack1ll11l1l1ll_opy_: TestFramework.bstack1ll111l1l1l_opy_,
                TestFramework.bstack1l1lll1l1ll_opy_: datetime.now(tz=timezone.utc),
                TestFramework.bstack1ll11l1ll1l_opy_: [],
                TestFramework.bstack1ll1l11ll11_opy_: hook_name,
                TestFramework.bstack1ll11l1l11l_opy_: bstack1ll1111l111_opy_.bstack1ll111l11l1_opy_()
            }
            bstack1l1lll1ll11_opy_[key].append(hook)
            bstack1ll11l11ll1_opy_[PytestBDDFramework.bstack1ll11111lll_opy_] = key
        elif test_hook_state == bstack1llll11l111_opy_.POST:
            bstack1ll1111l1l1_opy_ = bstack1l1lll1ll11_opy_.get(key, [])
            hook = bstack1ll1111l1l1_opy_.pop() if bstack1ll1111l1l1_opy_ else None
            if hook:
                result = self.__1ll1l11ll1l_opy_(*args)
                if result:
                    bstack1ll111ll11l_opy_ = result.get(bstack11lll1_opy_ (u"ࠤࡲࡹࡹࡩ࡯࡮ࡧࠥቍ"), TestFramework.bstack1ll111l1l1l_opy_)
                    if bstack1ll111ll11l_opy_ != TestFramework.bstack1ll111l1l1l_opy_:
                        hook[TestFramework.bstack1ll11l1l1ll_opy_] = bstack1ll111ll11l_opy_
                hook[TestFramework.bstack1l1llll1111_opy_] = datetime.now(tz=timezone.utc)
                hook[TestFramework.bstack1ll11l1l11l_opy_] = bstack1ll1111l111_opy_.bstack1ll111l11l1_opy_()
                self.bstack1ll1l111lll_opy_(hook)
                logs = hook.get(TestFramework.bstack1ll11l111l1_opy_, [])
                self.bstack1l1llllll1l_opy_(instance, logs)
                bstack1ll1111ll11_opy_[key].append(hook)
                bstack1ll11l11ll1_opy_[PytestBDDFramework.bstack1ll11ll1l1l_opy_] = key
        TestFramework.bstack1ll1l11lll1_opy_(instance, bstack1ll11l11ll1_opy_)
        self.logger.debug(bstack11lll1_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡ࡫ࡳࡴࡱ࡟ࡦࡸࡨࡲࡹࡀࠠࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦ࠿ࡾ࡯ࡪࡿࡽ࠯ࡽࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࢁࠥ࡮࡯ࡰ࡭ࡶࡣࡸࡺࡡࡳࡶࡨࡨࡂࢁࡨࡰࡱ࡮ࡷࡤࡹࡴࡢࡴࡷࡩࡩࢃࠠࡩࡱࡲ࡯ࡸࡥࡦࡪࡰ࡬ࡷ࡭࡫ࡤ࠾ࠤ቎") + str(bstack1ll1111ll11_opy_) + bstack11lll1_opy_ (u"ࠦࠧ቏"))
    def __1ll111llll1_opy_(
        self,
        context: bstack1ll111l11ll_opy_,
        test_framework_state: bstack1lll1l1ll11_opy_,
        test_hook_state: bstack1llll11l111_opy_,
        *args,
        **kwargs,
    ):
        fixturedef = TestFramework.bstack1ll1l11l11l_opy_(args[0], [bstack11lll1_opy_ (u"ࠧࡹࡣࡰࡲࡨࠦቐ"), bstack11lll1_opy_ (u"ࠨࡡࡳࡩࡱࡥࡲ࡫ࠢቑ"), bstack11lll1_opy_ (u"ࠢࡱࡣࡵࡥࡲࡹࠢቒ"), bstack11lll1_opy_ (u"ࠣ࡫ࡧࡷࠧቓ"), bstack11lll1_opy_ (u"ࠤࡸࡲ࡮ࡺࡴࡦࡵࡷࠦቔ"), bstack11lll1_opy_ (u"ࠥࡦࡦࡹࡥࡪࡦࠥቕ")]) if len(args) > 0 else {}
        request = args[1] if len(args) > 1 else None
        scenario = args[2] if len(args) == 3 else None
        scope = request.scope if hasattr(request, bstack11lll1_opy_ (u"ࠦࡸࡩ࡯ࡱࡧࠥቖ")) else fixturedef.get(bstack11lll1_opy_ (u"ࠧࡹࡣࡰࡲࡨࠦ቗"), None)
        fixturename = request.fixturename if hasattr(request, bstack11lll1_opy_ (u"ࠨࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࠦቘ")) else None
        node = request.node if hasattr(request, bstack11lll1_opy_ (u"ࠢ࡯ࡱࡧࡩࠧ቙")) else None
        target = request.node.nodeid if hasattr(node, bstack11lll1_opy_ (u"ࠣࡰࡲࡨࡪ࡯ࡤࠣቚ")) else None
        baseid = fixturedef.get(bstack11lll1_opy_ (u"ࠤࡥࡥࡸ࡫ࡩࡥࠤቛ"), None) or bstack11lll1_opy_ (u"ࠥࠦቜ")
        if (not target or len(baseid) > 0) and hasattr(request, bstack11lll1_opy_ (u"ࠦࡤࡶࡹࡧࡷࡱࡧ࡮ࡺࡥ࡮ࠤቝ")):
            target = PytestBDDFramework.__1ll111lll1l_opy_(request._pyfuncitem.location) if hasattr(request._pyfuncitem, bstack11lll1_opy_ (u"ࠧࡲ࡯ࡤࡣࡷ࡭ࡴࡴࠢ቞")) else None
            if target and not TestFramework.bstack1ll111l111l_opy_(target):
                self.__1ll111lllll_opy_(context, test_framework_state, target, (target, request._pyfuncitem.location))
                node = request._pyfuncitem
                self.logger.debug(bstack11lll1_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡬ࡩࡹࡶࡸࡶࡪࡥࡥࡷࡧࡱࡸ࠿ࠦࡦࡢ࡮࡯ࡦࡦࡩ࡫ࠡࡶࡤࡶ࡬࡫ࡴ࠾ࡽࡷࡥࡷ࡭ࡥࡵࡿࠣࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥ࠾ࡽࡩ࡭ࡽࡺࡵࡳࡧࡱࡥࡲ࡫ࡽࠡࡰࡲࡨࡪࡃࡻ࡯ࡱࡧࡩࢂࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࠣ቟") + str(test_hook_state) + bstack11lll1_opy_ (u"ࠢࠣበ"))
        if not fixturedef or not scope or not target:
            self.logger.warning(bstack11lll1_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡠࡧࡹࡩࡳࡺ࠺ࠡࡷࡱ࡬ࡦࡴࡤ࡭ࡧࡧࠤࡪࡼࡥ࡯ࡶࡀࡿࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁ࠳ࢁࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥࡾࠢࡩ࡭ࡽࡺࡵࡳࡧࡧࡩ࡫ࡃࡻࡧ࡫ࡻࡸࡺࡸࡥࡥࡧࡩࢁࠥࡹࡣࡰࡲࡨࡁࢀࡹࡣࡰࡲࡨࢁࠥࡺࡡࡳࡩࡨࡸࡂࠨቡ") + str(target) + bstack11lll1_opy_ (u"ࠤࠥቢ"))
            return None
        instance = TestFramework.bstack1ll111l111l_opy_(target)
        if not instance:
            self.logger.warning(bstack11lll1_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡩ࡭ࡽࡺࡵࡳࡧࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡹࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࡼࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࢀࠤ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦ࠿ࡾࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥࡾࠢࡶࡧࡴࡶࡥ࠾ࡽࡶࡧࡴࡶࡥࡾࠢࡥࡥࡸ࡫ࡩࡥ࠿ࡾࡦࡦࡹࡥࡪࡦࢀࠤࡹࡧࡲࡨࡧࡷࡁࠧባ") + str(target) + bstack11lll1_opy_ (u"ࠦࠧቤ"))
            return None
        bstack1ll1111llll_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll11ll1lll_opy_, {})
        if os.getenv(bstack11lll1_opy_ (u"࡙ࠧࡄࡌࡡࡆࡐࡎࡥࡆࡍࡃࡊࡣࡋࡏࡘࡕࡗࡕࡉࡘࠨብ"), bstack11lll1_opy_ (u"ࠨ࠱ࠣቦ")) == bstack11lll1_opy_ (u"ࠢ࠲ࠤቧ"):
            bstack1ll11l11111_opy_ = bstack11lll1_opy_ (u"ࠣ࠼ࠥቨ").join((scope, fixturename))
            bstack1ll1l11l111_opy_ = datetime.now(tz=timezone.utc)
            bstack1ll11111111_opy_ = {
                bstack11lll1_opy_ (u"ࠤ࡮ࡩࡾࠨቩ"): bstack1ll11l11111_opy_,
                bstack11lll1_opy_ (u"ࠥࡸࡦ࡭ࡳࠣቪ"): PytestBDDFramework.__1l1llll1l1l_opy_(request.node, scenario),
                bstack11lll1_opy_ (u"ࠦ࡫࡯ࡸࡵࡷࡵࡩࠧቫ"): fixturedef,
                bstack11lll1_opy_ (u"ࠧࡹࡣࡰࡲࡨࠦቬ"): scope,
                bstack11lll1_opy_ (u"ࠨࡴࡺࡲࡨࠦቭ"): None,
            }
            try:
                if test_hook_state == bstack1llll11l111_opy_.POST and callable(getattr(args[-1], bstack11lll1_opy_ (u"ࠢࡨࡧࡷࡣࡷ࡫ࡳࡶ࡮ࡷࠦቮ"), None)):
                    bstack1ll11111111_opy_[bstack11lll1_opy_ (u"ࠣࡶࡼࡴࡪࠨቯ")] = TestFramework.bstack1ll1l111l11_opy_(args[-1].get_result())
            except Exception as e:
                pass
            if test_hook_state == bstack1llll11l111_opy_.PRE:
                bstack1ll11111111_opy_[bstack11lll1_opy_ (u"ࠤࡸࡹ࡮ࡪࠢተ")] = uuid4().__str__()
                bstack1ll11111111_opy_[PytestBDDFramework.bstack1l1lll1l1ll_opy_] = bstack1ll1l11l111_opy_
            elif test_hook_state == bstack1llll11l111_opy_.POST:
                bstack1ll11111111_opy_[PytestBDDFramework.bstack1l1llll1111_opy_] = bstack1ll1l11l111_opy_
            if bstack1ll11l11111_opy_ in bstack1ll1111llll_opy_:
                bstack1ll1111llll_opy_[bstack1ll11l11111_opy_].update(bstack1ll11111111_opy_)
                self.logger.debug(bstack11lll1_opy_ (u"ࠥࡹࡵࡪࡡࡵࡧࡧࠤ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦ࠿ࡾࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥࡾࠢࡶࡧࡴࡶࡥ࠾ࡽࡶࡧࡴࡶࡥࡾࠢࡩ࡭ࡽࡺࡵࡳࡧࡀࠦቱ") + str(bstack1ll1111llll_opy_[bstack1ll11l11111_opy_]) + bstack11lll1_opy_ (u"ࠦࠧቲ"))
            else:
                bstack1ll1111llll_opy_[bstack1ll11l11111_opy_] = bstack1ll11111111_opy_
                self.logger.debug(bstack11lll1_opy_ (u"ࠧࡹࡡࡷࡧࡧࠤ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦ࠿ࡾࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥࡾࠢࡶࡧࡴࡶࡥ࠾ࡽࡶࡧࡴࡶࡥࡾࠢࡩ࡭ࡽࡺࡵࡳࡧࡀࡿࡹ࡫ࡳࡵࡡࡩ࡭ࡽࡺࡵࡳࡧࢀࠤࡹࡸࡡࡤ࡭ࡨࡨࡤ࡬ࡩࡹࡶࡸࡶࡪࡹ࠽ࠣታ") + str(len(bstack1ll1111llll_opy_)) + bstack11lll1_opy_ (u"ࠨࠢቴ"))
        TestFramework.bstack1lllll11l11_opy_(instance, PytestBDDFramework.bstack1ll11ll1lll_opy_, bstack1ll1111llll_opy_)
        self.logger.debug(bstack11lll1_opy_ (u"ࠢࡴࡣࡹࡩࡩࠦࡦࡪࡺࡷࡹࡷ࡫ࡳ࠾ࡽ࡯ࡩࡳ࠮ࡴࡳࡣࡦ࡯ࡪࡪ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡴࠫࢀࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࠢት") + str(instance.ref()) + bstack11lll1_opy_ (u"ࠣࠤቶ"))
        return instance
    def __1ll111lllll_opy_(
        self,
        context: bstack1ll111l11ll_opy_,
        test_framework_state: bstack1lll1l1ll11_opy_,
        target: Any,
        *args,
    ):
        ctx = bstack1ll1ll11l1l_opy_.create_context(target)
        ob = bstack1llll11111l_opy_(ctx, self.bstack1ll1l1l11ll_opy_, self.bstack1ll1l111ll1_opy_, test_framework_state)
        TestFramework.bstack1ll1l11lll1_opy_(ob, {
            TestFramework.bstack1lll1l11l11_opy_: context.test_framework_name,
            TestFramework.bstack1lll1ll11ll_opy_: context.test_framework_version,
            TestFramework.bstack1ll111ll111_opy_: [],
            PytestBDDFramework.bstack1ll11ll1lll_opy_: {},
            PytestBDDFramework.bstack1l1llll11l1_opy_: {},
            PytestBDDFramework.bstack1l1llll1ll1_opy_: {},
        })
        if len(args) > 1 and isinstance(args[1], tuple):
            TestFramework.bstack1lllll11l11_opy_(ob, TestFramework.bstack1ll11111ll1_opy_, str(args[1][0]))
        if context.platform_index >= 0:
            TestFramework.bstack1lllll11l11_opy_(ob, TestFramework.bstack1llll1ll111_opy_, context.platform_index)
        TestFramework.bstack1lll1lllll1_opy_[ctx.id] = ob
        self.logger.debug(bstack11lll1_opy_ (u"ࠤࡶࡥࡻ࡫ࡤࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࠣࡧࡹࡾ࠮ࡪࡦࡀࡿࡨࡺࡸ࠯࡫ࡧࢁࠥࡺࡡࡳࡩࡨࡸࡂࢁࡴࡢࡴࡪࡩࡹࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳ࠾ࠤቷ") + str(TestFramework.bstack1lll1lllll1_opy_.keys()) + bstack11lll1_opy_ (u"ࠥࠦቸ"))
        return ob
    @staticmethod
    def __1ll11ll1ll1_opy_(instance, args):
        request, feature, scenario = args
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack11lll1_opy_ (u"ࠫ࡮ࡪࠧቹ"): id(step),
                bstack11lll1_opy_ (u"ࠬࡺࡥࡹࡶࠪቺ"): step.name,
                bstack11lll1_opy_ (u"࠭࡫ࡦࡻࡺࡳࡷࡪࠧቻ"): step.keyword,
            })
        meta = {
            bstack11lll1_opy_ (u"ࠧࡧࡧࡤࡸࡺࡸࡥࠨቼ"): {
                bstack11lll1_opy_ (u"ࠨࡰࡤࡱࡪ࠭ች"): feature.name,
                bstack11lll1_opy_ (u"ࠩࡳࡥࡹ࡮ࠧቾ"): feature.filename,
                bstack11lll1_opy_ (u"ࠪࡨࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮ࠨቿ"): feature.description
            },
            bstack11lll1_opy_ (u"ࠫࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭ኀ"): {
                bstack11lll1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪኁ"): scenario.name
            },
            bstack11lll1_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬኂ"): steps,
            bstack11lll1_opy_ (u"ࠧࡦࡺࡤࡱࡵࡲࡥࡴࠩኃ"): PytestBDDFramework.__1ll11l1111l_opy_(request.node)
        }
        instance.data.update(
            {
                TestFramework.bstack1ll11ll111l_opy_: meta
            }
        )
    def bstack1ll1l111lll_opy_(self, hook: Dict[str, Any]) -> None:
        bstack11lll1_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡖࡲࡰࡥࡨࡷࡸ࡫ࡳࠡࡶ࡫ࡩࠥࡎ࡯ࡰ࡭ࡏࡩࡻ࡫࡬ࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸࠦࡳࡪ࡯࡬ࡰࡦࡸࠠࡵࡱࠣࡸ࡭࡫ࠠࡋࡣࡹࡥࠥ࡯࡭ࡱ࡮ࡨࡱࡪࡴࡴࡢࡶ࡬ࡳࡳ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡖ࡫࡭ࡸࠦ࡭ࡦࡶ࡫ࡳࡩࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥࡉࡨࡦࡥ࡮ࡷࠥࡺࡨࡦࠢࡋࡳࡴࡱࡌࡦࡸࡨࡰࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹࠡ࡫ࡱࡷ࡮ࡪࡥࠡࢀ࠲࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠲࡙ࡵࡲ࡯ࡢࡦࡨࡨࡆࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࡴ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡈࡲࡶࠥ࡫ࡡࡤࡪࠣࡪ࡮ࡲࡥࠡ࡫ࡱࠤ࡭ࡵ࡯࡬ࡡ࡯ࡩࡻ࡫࡬ࡠࡨ࡬ࡰࡪࡹࠬࠡࡴࡨࡴࡱࡧࡣࡦࡵ࡙ࠣࠦ࡫ࡳࡵࡎࡨࡺࡪࡲࠢࠡࡹ࡬ࡸ࡭ࠦࠢࡉࡱࡲ࡯ࡑ࡫ࡶࡦ࡮ࠥࠤ࡮ࡴࠠࡪࡶࡶࠤࡵࡧࡴࡩ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡋࡩࠤࡦࠦࡦࡪ࡮ࡨࠤ࡮ࡴࠠࡵࡪࡨࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠠ࡮ࡣࡷࡧ࡭࡫ࡳࠡࡣࠣࡱࡴࡪࡩࡧ࡫ࡨࡨࠥ࡮࡯ࡰ࡭࠰ࡰࡪࡼࡥ࡭ࠢࡩ࡭ࡱ࡫ࠬࠡ࡫ࡷࠤࡨࡸࡥࡢࡶࡨࡷࠥࡧࠠࡍࡱࡪࡉࡳࡺࡲࡺࠢࡲࡦ࡯࡫ࡣࡵࠢࡺ࡭ࡹ࡮ࠠࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࠤࡩ࡫ࡴࡢ࡫࡯ࡷ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤࡘ࡯࡭ࡪ࡮ࡤࡶࡱࡿࠬࠡ࡫ࡷࠤࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠠࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࠤࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࡴࠢ࡯ࡳࡨࡧࡴࡦࡦࠣ࡭ࡳࠦࡈࡰࡱ࡮ࡐࡪࡼࡥ࡭࠱ࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࡎ࡯ࡰ࡭ࡈࡺࡪࡴࡴࠡࡤࡼࠤࡷ࡫ࡰ࡭ࡣࡦ࡭ࡳ࡭ࠠࠣࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࠧࠦࡷࡪࡶ࡫ࠤࠧࡎ࡯ࡰ࡭ࡏࡩࡻ࡫࡬࠰ࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࡍࡵ࡯࡬ࡇࡹࡩࡳࡺࠢ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠳ࠠࡕࡪࡨࠤࡨࡸࡥࡢࡶࡨࡨࠥࡒ࡯ࡨࡇࡱࡸࡷࡿࠠࡰࡤ࡭ࡩࡨࡺࡳࠡࡣࡵࡩࠥࡧࡤࡥࡧࡧࠤࡹࡵࠠࡵࡪࡨࠤ࡭ࡵ࡯࡬ࠩࡶࠤࠧࡲ࡯ࡨࡵࠥࠤࡱ࡯ࡳࡵ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡆࡸࡧࡴ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡪࡲࡳࡰࡀࠠࡕࡪࡨࠤࡪࡼࡥ࡯ࡶࠣࡨ࡮ࡩࡴࡪࡱࡱࡥࡷࡿࠠࡤࡱࡱࡸࡦ࡯࡮ࡪࡰࡪࠤࡪࡾࡩࡴࡶ࡬ࡲ࡬ࠦ࡬ࡰࡩࡶࠤࡦࡴࡤࠡࡪࡲࡳࡰࠦࡩ࡯ࡨࡲࡶࡲࡧࡴࡪࡱࡱ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࡬ࡴࡵ࡫ࡠ࡮ࡨࡺࡪࡲ࡟ࡧ࡫࡯ࡩࡸࡀࠠࡍ࡫ࡶࡸࠥࡵࡦࠡࡒࡤࡸ࡭ࠦ࡯ࡣ࡬ࡨࡧࡹࡹࠠࡧࡴࡲࡱࠥࡺࡨࡦࠢࡗࡩࡸࡺࡌࡦࡸࡨࡰࠥࡳ࡯࡯࡫ࡷࡳࡷ࡯࡮ࡨ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡤࡸ࡭ࡱࡪ࡟࡭ࡧࡹࡩࡱࡥࡦࡪ࡮ࡨࡷ࠿ࠦࡌࡪࡵࡷࠤࡴ࡬ࠠࡑࡣࡷ࡬ࠥࡵࡢ࡫ࡧࡦࡸࡸࠦࡦࡳࡱࡰࠤࡹ࡮ࡥࠡࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࠥࡳ࡯࡯࡫ࡷࡳࡷ࡯࡮ࡨ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢኄ")
        global _1ll1l1111l1_opy_
        platform_index = os.environ[bstack11lll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩኅ")]
        bstack1ll1l11l1ll_opy_ = os.path.join(bstack1ll11lll11l_opy_, (bstack1ll1111l1ll_opy_ + str(platform_index)), bstack1ll11l11lll_opy_)
        if not os.path.exists(bstack1ll1l11l1ll_opy_) or not os.path.isdir(bstack1ll1l11l1ll_opy_):
            return
        logs = hook.get(bstack11lll1_opy_ (u"ࠥࡰࡴ࡭ࡳࠣኆ"), [])
        with os.scandir(bstack1ll1l11l1ll_opy_) as entries:
            for entry in entries:
                abs_path = os.path.abspath(entry.path)
                if abs_path in _1ll1l1111l1_opy_:
                    self.logger.info(bstack11lll1_opy_ (u"ࠦࡕࡧࡴࡩࠢࡤࡰࡷ࡫ࡡࡥࡻࠣࡴࡷࡵࡣࡦࡵࡶࡩࡩࠦࡻࡾࠤኇ").format(abs_path))
                    continue
                if entry.is_file():
                    try:
                        timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                    except Exception:
                        timestamp = bstack11lll1_opy_ (u"ࠧࠨኈ")
                    log_entry = bstack1l1lllll111_opy_(
                        kind=bstack11lll1_opy_ (u"ࠨࡔࡆࡕࡗࡣࡆ࡚ࡔࡂࡅࡋࡑࡊࡔࡔࠣ኉"),
                        message=bstack11lll1_opy_ (u"ࠢࠣኊ"),
                        level=bstack11lll1_opy_ (u"ࠣࠤኋ"),
                        timestamp=timestamp,
                        fileName=entry.name,
                        bstack1l1lll1llll_opy_=entry.stat().st_size,
                        bstack1l1lllllll1_opy_=bstack11lll1_opy_ (u"ࠤࡐࡅࡓ࡛ࡁࡍࡡࡘࡔࡑࡕࡁࡅࠤኌ"),
                        bstack11l111l_opy_=os.path.abspath(entry.path),
                        bstack1ll11l11l11_opy_=hook.get(TestFramework.bstack1ll11l1llll_opy_)
                    )
                    logs.append(log_entry)
                    _1ll1l1111l1_opy_.add(abs_path)
        platform_index = os.environ[bstack11lll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪኍ")]
        bstack1ll11l1l1l1_opy_ = os.path.join(bstack1ll11lll11l_opy_, (bstack1ll1111l1ll_opy_ + str(platform_index)), bstack1ll11l11lll_opy_, bstack1ll111ll1ll_opy_)
        if not os.path.exists(bstack1ll11l1l1l1_opy_) or not os.path.isdir(bstack1ll11l1l1l1_opy_):
            self.logger.info(bstack11lll1_opy_ (u"ࠦࡓࡵࠠࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࡌࡴࡵ࡫ࡆࡸࡨࡲࡹࠦࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࡶࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠠࡧࡱࡸࡲࡩࠦࡡࡵ࠼ࠣࡿࢂࠨ኎").format(bstack1ll11l1l1l1_opy_))
        else:
            self.logger.info(bstack11lll1_opy_ (u"ࠧࡖࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࡎ࡯ࡰ࡭ࡈࡺࡪࡴࡴࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸࠦࡦࡳࡱࡰࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿ࠺ࠡࡽࢀࠦ኏").format(bstack1ll11l1l1l1_opy_))
            with os.scandir(bstack1ll11l1l1l1_opy_) as entries:
                for entry in entries:
                    abs_path = os.path.abspath(entry.path)
                    if abs_path in _1ll1l1111l1_opy_:
                        self.logger.info(bstack11lll1_opy_ (u"ࠨࡐࡢࡶ࡫ࠤࡦࡲࡲࡦࡣࡧࡽࠥࡶࡲࡰࡥࡨࡷࡸ࡫ࡤࠡࡽࢀࠦነ").format(abs_path))
                        continue
                    if entry.is_file():
                        try:
                            timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                        except Exception:
                            timestamp = bstack11lll1_opy_ (u"ࠢࠣኑ")
                        log_entry = bstack1l1lllll111_opy_(
                            kind=bstack11lll1_opy_ (u"ࠣࡖࡈࡗ࡙ࡥࡁࡕࡖࡄࡇࡍࡓࡅࡏࡖࠥኒ"),
                            message=bstack11lll1_opy_ (u"ࠤࠥና"),
                            level=bstack11lll1_opy_ (u"ࠥࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࠢኔ"),
                            timestamp=timestamp,
                            fileName=entry.name,
                            bstack1l1lll1llll_opy_=entry.stat().st_size,
                            bstack1l1lllllll1_opy_=bstack11lll1_opy_ (u"ࠦࡒࡇࡎࡖࡃࡏࡣ࡚ࡖࡌࡐࡃࡇࠦን"),
                            bstack11l111l_opy_=os.path.abspath(entry.path),
                            bstack1ll1l1l1111_opy_=hook.get(TestFramework.bstack1ll11l1llll_opy_)
                        )
                        logs.append(log_entry)
                        _1ll1l1111l1_opy_.add(abs_path)
        hook[bstack11lll1_opy_ (u"ࠧࡲ࡯ࡨࡵࠥኖ")] = logs
    def bstack1l1llllll1l_opy_(
        self,
        bstack1ll111lll11_opy_: bstack1llll11111l_opy_,
        entries: List[bstack1l1lllll111_opy_],
    ):
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = os.environ.get(bstack11lll1_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡌࡊࡡࡅࡍࡓࡥࡓࡆࡕࡖࡍࡔࡔ࡟ࡊࡆࠥኗ"))
        req.platform_index = TestFramework.get_state(bstack1ll111lll11_opy_, TestFramework.bstack1llll1ll111_opy_)
        req.execution_context.hash = str(bstack1ll111lll11_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll111lll11_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll111lll11_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1ll111lll11_opy_, TestFramework.bstack1lll1l11l11_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1ll111lll11_opy_, TestFramework.bstack1lll1ll11ll_opy_)
            log_entry.uuid = entry.bstack1ll11l11l11_opy_ if entry.bstack1ll11l11l11_opy_ else TestFramework.get_state(bstack1ll111lll11_opy_, TestFramework.bstack1lll11ll111_opy_)
            log_entry.test_framework_state = bstack1ll111lll11_opy_.state.name
            log_entry.message = entry.message.encode(bstack11lll1_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨኘ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            if isinstance(entry.level, str) and len(entry.level.strip()) > 0:
                log_entry.level = entry.level.strip()
            if entry.kind == bstack11lll1_opy_ (u"ࠣࡖࡈࡗ࡙ࡥࡁࡕࡖࡄࡇࡍࡓࡅࡏࡖࠥኙ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1l1lll1llll_opy_
                log_entry.file_path = entry.bstack11l111l_opy_
        def bstack1l1llll111l_opy_():
            bstack11l11lll1l_opy_ = datetime.now()
            try:
                self.bstack1llll11lll1_opy_.LogCreatedEvent(req)
                bstack1ll111lll11_opy_.bstack1lllll11ll_opy_(bstack11lll1_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡴࡧࡱࡨࡤࡲ࡯ࡨࡡࡦࡶࡪࡧࡴࡦࡦࡢࡩࡻ࡫࡮ࡵࡡࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࠨኚ"), datetime.now() - bstack11l11lll1l_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack11lll1_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࡴࡧࡱࡨࡤࡲ࡯ࡨࡡࡦࡶࡪࡧࡴࡦࡦࡢࡩࡻ࡫࡮ࡵࡡࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࠦࡻࡾࠤኛ").format(str(e)))
                traceback.print_exc()
        self.bstack1lll11l1l1l_opy_.enqueue(bstack1l1llll111l_opy_)
    def __1ll11lllll1_opy_(self, instance) -> None:
        bstack11lll1_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡎࡲࡥࡩࡹࠠࡤࡷࡶࡸࡴࡳࠠࡵࡣࡪࡷࠥ࡬࡯ࡳࠢࡷ࡬ࡪࠦࡧࡪࡸࡨࡲࠥࡺࡥࡴࡶࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡇࡷ࡫ࡡࡵࡧࡶࠤࡦࠦࡤࡪࡥࡷࠤࡨࡵ࡮ࡵࡣ࡬ࡲ࡮ࡴࡧࠡࡶࡨࡷࡹࠦ࡬ࡦࡸࡨࡰࠥࡩࡵࡴࡶࡲࡱࠥࡳࡥࡵࡣࡧࡥࡹࡧࠠࡳࡧࡷࡶ࡮࡫ࡶࡦࡦࠣࡪࡷࡵ࡭ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡆࡹࡸࡺ࡯࡮ࡖࡤ࡫ࡒࡧ࡮ࡢࡩࡨࡶࠥࡧ࡮ࡥࠢࡸࡴࡩࡧࡴࡦࡵࠣࡸ࡭࡫ࠠࡪࡰࡶࡸࡦࡴࡣࡦࠢࡶࡸࡦࡺࡥࠡࡷࡶ࡭ࡳ࡭ࠠࡴࡧࡷࡣࡸࡺࡡࡵࡧࡢࡩࡳࡺࡲࡪࡧࡶ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤኜ")
        bstack1ll11l11ll1_opy_ = {bstack11lll1_opy_ (u"ࠧࡩࡵࡴࡶࡲࡱࡤࡳࡥࡵࡣࡧࡥࡹࡧࠢኝ"): bstack1ll1111l111_opy_.bstack1ll111l11l1_opy_()}
        TestFramework.bstack1ll1l11lll1_opy_(instance, bstack1ll11l11ll1_opy_)
    @staticmethod
    def __1ll1l1l11l1_opy_(instance, args):
        request, bstack1ll11l1ll11_opy_ = args
        bstack1ll1l1ll111_opy_ = id(bstack1ll11l1ll11_opy_)
        bstack1ll11l1l111_opy_ = instance.data[TestFramework.bstack1ll11ll111l_opy_]
        step = next(filter(lambda st: st[bstack11lll1_opy_ (u"࠭ࡩࡥࠩኞ")] == bstack1ll1l1ll111_opy_, bstack1ll11l1l111_opy_[bstack11lll1_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ኟ")]), None)
        step.update({
            bstack11lll1_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬአ"): datetime.now(tz=timezone.utc)
        })
        index = next((i for i, st in enumerate(bstack1ll11l1l111_opy_[bstack11lll1_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨኡ")]) if st[bstack11lll1_opy_ (u"ࠪ࡭ࡩ࠭ኢ")] == step[bstack11lll1_opy_ (u"ࠫ࡮ࡪࠧኣ")]), None)
        if index is not None:
            bstack1ll11l1l111_opy_[bstack11lll1_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫኤ")][index] = step
        instance.data[TestFramework.bstack1ll11ll111l_opy_] = bstack1ll11l1l111_opy_
    @staticmethod
    def __1ll11ll1111_opy_(instance, args):
        bstack11lll1_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡻ࡭࡫࡮ࠡ࡮ࡨࡲࠥࡧࡲࡨࡵࠣ࡭ࡸࠦ࠲࠭ࠢ࡬ࡸࠥࡹࡩࡨࡰ࡬ࡪ࡮࡫ࡳࠡࡶ࡫ࡩࡷ࡫ࠠࡪࡵࠣࡲࡴࠦࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡢࡴࡪࡷࠥࡧࡲࡦࠢ࠰ࠤࡠࡸࡥࡲࡷࡨࡷࡹ࠲ࠠࡴࡶࡨࡴࡢࠐࠠࠡࠢࠣࠤࠥࠦࠠࡪࡨࠣࡥࡷ࡭ࡳࠡࡣࡵࡩࠥ࠹ࠠࡵࡪࡨࡲࠥࡺࡨࡦࠢ࡯ࡥࡸࡺࠠࡷࡣ࡯ࡹࡪࠦࡩࡴࠢࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤእ")
        bstack1ll11l11l1l_opy_ = datetime.now(tz=timezone.utc)
        request = args[0]
        bstack1ll11l1ll11_opy_ = args[1]
        bstack1ll1l1ll111_opy_ = id(bstack1ll11l1ll11_opy_)
        bstack1ll11l1l111_opy_ = instance.data[TestFramework.bstack1ll11ll111l_opy_]
        step = None
        if bstack1ll1l1ll111_opy_ is not None and bstack1ll11l1l111_opy_.get(bstack11lll1_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ኦ")):
            step = next(filter(lambda st: st[bstack11lll1_opy_ (u"ࠨ࡫ࡧࠫኧ")] == bstack1ll1l1ll111_opy_, bstack1ll11l1l111_opy_[bstack11lll1_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨከ")]), None)
            step.update({
                bstack11lll1_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨኩ"): bstack1ll11l11l1l_opy_,
            })
        if len(args) > 2:
            exception = args[2]
            step.update({
                bstack11lll1_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫኪ"): bstack11lll1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬካ"),
                bstack11lll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫ࠧኬ"): str(exception)
            })
        else:
            if step is not None:
                step.update({
                    bstack11lll1_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧክ"): bstack11lll1_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨኮ"),
                })
        index = next((i for i, st in enumerate(bstack1ll11l1l111_opy_[bstack11lll1_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨኯ")]) if st[bstack11lll1_opy_ (u"ࠪ࡭ࡩ࠭ኰ")] == step[bstack11lll1_opy_ (u"ࠫ࡮ࡪࠧ኱")]), None)
        if index is not None:
            bstack1ll11l1l111_opy_[bstack11lll1_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫኲ")][index] = step
        instance.data[TestFramework.bstack1ll11ll111l_opy_] = bstack1ll11l1l111_opy_
    @staticmethod
    def __1ll11l1111l_opy_(node):
        try:
            examples = []
            if hasattr(node, bstack11lll1_opy_ (u"࠭ࡣࡢ࡮࡯ࡷࡵ࡫ࡣࠨኳ")):
                examples = list(node.callspec.params[bstack11lll1_opy_ (u"ࠧࡠࡲࡼࡸࡪࡹࡴࡠࡤࡧࡨࡤ࡫ࡸࡢ࡯ࡳࡰࡪ࠭ኴ")].values())
            return examples
        except:
            return []
    def bstack1l1lllll11l_opy_(self, instance: bstack1llll11111l_opy_, bstack1llll1lll1l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1llll11l111_opy_]):
        bstack1l1llllllll_opy_ = (
            PytestBDDFramework.bstack1ll11111lll_opy_
            if bstack1llll1lll1l_opy_[1] == bstack1llll11l111_opy_.PRE
            else PytestBDDFramework.bstack1ll11ll1l1l_opy_
        )
        hook = PytestBDDFramework.bstack1ll11l111ll_opy_(instance, bstack1l1llllllll_opy_)
        entries = hook.get(TestFramework.bstack1ll11l1ll1l_opy_, []) if isinstance(hook, dict) else []
        entries.extend(TestFramework.get_state(instance, TestFramework.bstack1ll111ll111_opy_, []))
        return entries
    def bstack1ll111111l1_opy_(self, instance: bstack1llll11111l_opy_, bstack1llll1lll1l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1llll11l111_opy_]):
        bstack1l1llllllll_opy_ = (
            PytestBDDFramework.bstack1ll11111lll_opy_
            if bstack1llll1lll1l_opy_[1] == bstack1llll11l111_opy_.PRE
            else PytestBDDFramework.bstack1ll11ll1l1l_opy_
        )
        PytestBDDFramework.bstack1ll1l1l111l_opy_(instance, bstack1l1llllllll_opy_)
        TestFramework.get_state(instance, TestFramework.bstack1ll111ll111_opy_, []).clear()
    @staticmethod
    def bstack1ll11l111ll_opy_(instance: bstack1llll11111l_opy_, bstack1l1llllllll_opy_: str):
        bstack1ll11lll1ll_opy_ = (
            PytestBDDFramework.bstack1l1llll11l1_opy_
            if bstack1l1llllllll_opy_ == PytestBDDFramework.bstack1ll11ll1l1l_opy_
            else PytestBDDFramework.bstack1l1llll1ll1_opy_
        )
        bstack1ll1l1l1l11_opy_ = TestFramework.get_state(instance, bstack1l1llllllll_opy_, None)
        bstack1l1lllll1l1_opy_ = TestFramework.get_state(instance, bstack1ll11lll1ll_opy_, None) if bstack1ll1l1l1l11_opy_ else None
        return (
            bstack1l1lllll1l1_opy_[bstack1ll1l1l1l11_opy_][-1]
            if isinstance(bstack1l1lllll1l1_opy_, dict) and len(bstack1l1lllll1l1_opy_.get(bstack1ll1l1l1l11_opy_, [])) > 0
            else None
        )
    @staticmethod
    def bstack1ll1l1l111l_opy_(instance: bstack1llll11111l_opy_, bstack1l1llllllll_opy_: str):
        hook = PytestBDDFramework.bstack1ll11l111ll_opy_(instance, bstack1l1llllllll_opy_)
        if isinstance(hook, dict):
            hook.get(TestFramework.bstack1ll11l1ll1l_opy_, []).clear()
    @staticmethod
    def __1ll11lll111_opy_(instance: bstack1llll11111l_opy_, *args):
        if len(args) < 2 or not callable(getattr(args[1], bstack11lll1_opy_ (u"ࠣࡩࡨࡸࡤࡸࡥࡤࡱࡵࡨࡸࠨኵ"), None)):
            return
        if os.getenv(bstack11lll1_opy_ (u"ࠤࡖࡈࡐࡥࡃࡍࡋࡢࡊࡑࡇࡇࡠࡎࡒࡋࡘࠨ኶"), bstack11lll1_opy_ (u"ࠥ࠵ࠧ኷")) != bstack11lll1_opy_ (u"ࠦ࠶ࠨኸ"):
            PytestBDDFramework.logger.warning(bstack11lll1_opy_ (u"ࠧ࡯ࡧ࡯ࡱࡵ࡭ࡳ࡭ࠠࡤࡣࡳࡰࡴ࡭ࠢኹ"))
            return
        bstack1ll1l1l1lll_opy_ = {
            bstack11lll1_opy_ (u"ࠨࡳࡦࡶࡸࡴࠧኺ"): (PytestBDDFramework.bstack1ll11111lll_opy_, PytestBDDFramework.bstack1l1llll1ll1_opy_),
            bstack11lll1_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࠤኻ"): (PytestBDDFramework.bstack1ll11ll1l1l_opy_, PytestBDDFramework.bstack1l1llll11l1_opy_),
        }
        for when in (bstack11lll1_opy_ (u"ࠣࡵࡨࡸࡺࡶࠢኼ"), bstack11lll1_opy_ (u"ࠤࡦࡥࡱࡲࠢኽ"), bstack11lll1_opy_ (u"ࠥࡸࡪࡧࡲࡥࡱࡺࡲࠧኾ")):
            bstack1ll1l111111_opy_ = args[1].get_records(when)
            if not bstack1ll1l111111_opy_:
                continue
            records = [
                bstack1l1lllll111_opy_(
                    kind=TestFramework.bstack1ll11llll11_opy_,
                    message=r.message,
                    level=r.levelname if hasattr(r, bstack11lll1_opy_ (u"ࠦࡱ࡫ࡶࡦ࡮ࡱࡥࡲ࡫ࠢ኿")) and r.levelname else None,
                    timestamp=(
                        datetime.fromtimestamp(r.created, tz=timezone.utc)
                        if hasattr(r, bstack11lll1_opy_ (u"ࠧࡩࡲࡦࡣࡷࡩࡩࠨዀ")) and r.created
                        else None
                    ),
                )
                for r in bstack1ll1l111111_opy_
                if isinstance(getattr(r, bstack11lll1_opy_ (u"ࠨ࡭ࡦࡵࡶࡥ࡬࡫ࠢ዁"), None), str) and r.message.strip()
            ]
            if not records:
                continue
            bstack1ll1111ll1l_opy_, bstack1ll11lll1ll_opy_ = bstack1ll1l1l1lll_opy_.get(when, (None, None))
            bstack1ll1l11111l_opy_ = TestFramework.get_state(instance, bstack1ll1111ll1l_opy_, None) if bstack1ll1111ll1l_opy_ else None
            bstack1l1lllll1l1_opy_ = TestFramework.get_state(instance, bstack1ll11lll1ll_opy_, None) if bstack1ll1l11111l_opy_ else None
            if isinstance(bstack1l1lllll1l1_opy_, dict) and len(bstack1l1lllll1l1_opy_.get(bstack1ll1l11111l_opy_, [])) > 0:
                hook = bstack1l1lllll1l1_opy_[bstack1ll1l11111l_opy_][-1]
                if isinstance(hook, dict) and TestFramework.bstack1ll11l1ll1l_opy_ in hook:
                    hook[TestFramework.bstack1ll11l1ll1l_opy_].extend(records)
                    continue
            logs = TestFramework.get_state(instance, TestFramework.bstack1ll111ll111_opy_, [])
            logs.extend(records)
    @staticmethod
    def __1ll1l11l1l1_opy_(args) -> Dict[str, Any]:
        request, feature, scenario = args
        test_id = request.node.nodeid
        test_name = PytestBDDFramework.__1ll11ll11l1_opy_(request.node, scenario)
        bstack1ll1111111l_opy_ = feature.filename
        if not test_id or not test_name or not bstack1ll1111111l_opy_:
            return None
        code = None
        return {
            TestFramework.bstack1lll11ll111_opy_: uuid4().__str__(),
            TestFramework.bstack1ll11llll1l_opy_: test_id,
            TestFramework.bstack1ll11l1lll1_opy_: test_name,
            TestFramework.bstack1ll111111ll_opy_: test_id,
            TestFramework.bstack1ll1l11llll_opy_: bstack1ll1111111l_opy_,
            TestFramework.bstack1ll1l1l1l1l_opy_: PytestBDDFramework.__1l1llll1l1l_opy_(feature, scenario),
            TestFramework.bstack1ll11ll1l11_opy_: code,
            TestFramework.bstack1lll1ll111l_opy_: TestFramework.bstack1ll111l1l11_opy_,
            TestFramework.bstack1lll111l1l1_opy_: test_name
        }
    @staticmethod
    def __1ll11ll11l1_opy_(node, scenario):
        if hasattr(node, bstack11lll1_opy_ (u"ࠧࡤࡣ࡯ࡰࡸࡶࡥࡤࠩዂ")):
            parts = node.nodeid.rsplit(bstack11lll1_opy_ (u"ࠣ࡝ࠥዃ"))
            params = parts[-1]
            return bstack11lll1_opy_ (u"ࠤࡾࢁࠥࡡࡻࡾࠤዄ").format(scenario.name, params)
        return scenario.name
    @staticmethod
    def __1l1llll1l1l_opy_(feature, scenario) -> List[str]:
        return (list(feature.tags) if hasattr(feature, bstack11lll1_opy_ (u"ࠪࡸࡦ࡭ࡳࠨዅ")) else []) + (list(scenario.tags) if hasattr(scenario, bstack11lll1_opy_ (u"ࠫࡹࡧࡧࡴࠩ዆")) else [])
    @staticmethod
    def __1ll111lll1l_opy_(location):
        return bstack11lll1_opy_ (u"ࠧࡀ࠺ࠣ዇").join(filter(lambda x: isinstance(x, str), location))