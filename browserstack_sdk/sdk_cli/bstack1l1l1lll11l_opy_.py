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
import os
from datetime import datetime, timezone
from uuid import uuid4
from typing import Dict, List, Any, Tuple
from browserstack_sdk.sdk_cli.bstack1ll1llllll1_opy_ import bstack1ll1ll11l1l_opy_
from browserstack_sdk.sdk_cli.utils.bstack111l1111l1_opy_ import bstack1ll11l11lll_opy_
from browserstack_sdk.sdk_cli.test_framework import (
    TestFramework,
    bstack1lll1l11lll_opy_,
    bstack1llll111111_opy_,
    bstack1lll11lll11_opy_,
    bstack1ll11l1llll_opy_,
    bstack1l1lllll1ll_opy_,
)
from pathlib import Path
import grpc
from browserstack_sdk import sdk_pb2 as structs
from datetime import datetime, timezone
from typing import List, Dict, Any
import traceback
from bstack_utils.helper import bstack1ll1l111111_opy_
from bstack_utils.bstack1ll1ll1lll_opy_ import bstack1llll1l1l1l_opy_
from bstack_utils.constants import EVENTS
from browserstack_sdk.sdk_cli.bstack1lll11l1l1l_opy_ import bstack1lll11l1l11_opy_
from browserstack_sdk.sdk_cli.utils.bstack1ll11111ll1_opy_ import bstack1ll1l1l1ll1_opy_
from bstack_utils.bstack1l1l111l_opy_ import bstack1l11111l_opy_
bstack1ll1l11lll1_opy_ = bstack1ll1l111111_opy_()
bstack1ll1l1l1l1l_opy_ = 1.0
bstack1ll11ll1l1l_opy_ = bstack1lll11l_opy_ (u"ࠤࡘࡴࡱࡵࡡࡥࡧࡧࡅࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳ࠮ࠤᖎ")
bstack11lll1llll1_opy_ = bstack1lll11l_opy_ (u"ࠥࡘࡪࡹࡴࡍࡧࡹࡩࡱࠨᖏ")
bstack11lll1lll1l_opy_ = bstack1lll11l_opy_ (u"ࠦࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࠣᖐ")
bstack11lll1lll11_opy_ = bstack1lll11l_opy_ (u"ࠧࡎ࡯ࡰ࡭ࡏࡩࡻ࡫࡬ࠣᖑ")
bstack11lll1ll1ll_opy_ = bstack1lll11l_opy_ (u"ࠨࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࡋࡳࡴࡱࡅࡷࡧࡱࡸࠧᖒ")
_1ll111l1111_opy_ = set()
class bstack1l11lll1lll_opy_(TestFramework):
    bstack1ll11lll111_opy_ = bstack1lll11l_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡬ࡩࡹࡶࡸࡶࡪࡹࠢᖓ")
    bstack1ll1l11ll1l_opy_ = bstack1lll11l_opy_ (u"ࠣࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡷࡤࡹࡴࡢࡴࡷࡩࡩࠨᖔ")
    bstack1ll1l11l111_opy_ = bstack1lll11l_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡸࡥࡦࡪࡰ࡬ࡷ࡭࡫ࡤࠣᖕ")
    bstack1l1lllllll1_opy_ = bstack1lll11l_opy_ (u"ࠥࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥ࡬ࡢࡵࡷࡣࡸࡺࡡࡳࡶࡨࡨࠧᖖ")
    bstack1ll111l111l_opy_ = bstack1lll11l_opy_ (u"ࠦࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟࡭ࡣࡶࡸࡤ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪࠢᖗ")
    bstack1ll1l1l1111_opy_: bool
    bstack1lll11l1l1l_opy_: bstack1lll11l1l11_opy_  = None
    bstack1llll11l11l_opy_ = None
    bstack1ll11ll1lll_opy_ = [
        bstack1lll1l11lll_opy_.BEFORE_ALL,
        bstack1lll1l11lll_opy_.AFTER_ALL,
        bstack1lll1l11lll_opy_.BEFORE_EACH,
        bstack1lll1l11lll_opy_.AFTER_EACH,
    ]
    def __init__(
        self,
        bstack1ll111llll1_opy_: Dict[str, str],
        bstack1l1llllll11_opy_: List[str]=[bstack1lll11l_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸࠧᖘ")],
        bstack1lll11l1l1l_opy_: bstack1lll11l1l11_opy_=None,
        bstack1llll11l11l_opy_=None
    ):
        super().__init__(bstack1l1llllll11_opy_, bstack1ll111llll1_opy_, bstack1lll11l1l1l_opy_)
        self.bstack1ll1l1l1111_opy_ = any(bstack1lll11l_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹࠨᖙ") in item.lower() for item in bstack1l1llllll11_opy_)
        self.bstack1llll11l11l_opy_ = bstack1llll11l11l_opy_
    def track_event(
        self,
        context: bstack1ll11l1llll_opy_,
        test_framework_state: bstack1lll1l11lll_opy_,
        test_hook_state: bstack1lll11lll11_opy_,
        *args,
        **kwargs,
    ):
        super().track_event(self, context, test_framework_state, test_hook_state, *args, **kwargs)
        if test_framework_state == bstack1lll1l11lll_opy_.TEST or test_framework_state in bstack1l11lll1lll_opy_.bstack1ll11ll1lll_opy_:
            bstack1ll11l11lll_opy_(test_framework_state, test_hook_state)
        if test_framework_state == bstack1lll1l11lll_opy_.NONE:
            self.logger.warning(bstack1lll11l_opy_ (u"ࠢࡪࡩࡱࡳࡷ࡫ࡤࠡࡥࡤࡰࡱࡨࡡࡤ࡭ࠣࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࡀࡿࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁࠥࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫࠽ࠣᖚ") + str(test_hook_state) + bstack1lll11l_opy_ (u"ࠣࠤᖛ"))
            return
        if not self.bstack1ll1l1l1111_opy_:
            self.logger.warning(bstack1lll11l_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡧࡹࡩࡳࡺ࠺ࠡࡷࡱࡷࡺࡶࡰࡰࡴࡷࡩࡩࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬࠿ࠥᖜ") + str(str(self.bstack1l1llllll11_opy_)) + bstack1lll11l_opy_ (u"ࠥࠦᖝ"))
            return
        if not isinstance(args, tuple) or len(args) == 0:
            self.logger.warning(bstack1lll11l_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡹࡳ࡫ࡸࡱࡧࡦࡸࡪࡪࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᖞ") + str(kwargs) + bstack1lll11l_opy_ (u"ࠧࠨᖟ"))
            return
        instance = self.__1ll11ll111l_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        if not instance:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡻ࡮ࡩࡣࡱࡨࡱ࡫ࡤࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࡾࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࢂࠦࡡࡳࡩࡶࡁࠧᖠ") + str(args) + bstack1lll11l_opy_ (u"ࠢࠣᖡ"))
            return
        try:
            if instance!= None and test_framework_state in bstack1l11lll1lll_opy_.bstack1ll11ll1lll_opy_ and test_hook_state == bstack1lll11lll11_opy_.PRE:
                bstack1ll111111l1_opy_ = bstack1llll1l1l1l_opy_.bstack1ll111l1ll1_opy_(EVENTS.bstack1ll1l1l111_opy_.value)
                name = str(EVENTS.bstack1ll1l1l111_opy_.name)+bstack1lll11l_opy_ (u"ࠣ࠼ࠥᖢ")+str(test_framework_state.name)
                TestFramework.bstack1l1llllllll_opy_(instance, name, bstack1ll111111l1_opy_)
        except Exception as e:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡪࡲࡳࡰࠦࡥࡳࡴࡲࡶࠥࡶࡲࡦ࠼ࠣࡿࢂࠨᖣ").format(e))
        try:
            if not TestFramework.bstack1llll11ll11_opy_(instance, TestFramework.bstack1ll11l1l1l1_opy_) and test_hook_state == bstack1lll11lll11_opy_.PRE:
                test = bstack1l11lll1lll_opy_.__1ll11lll1ll_opy_(args[0])
                if test:
                    instance.data.update(test)
                    self.logger.debug(bstack1lll11l_opy_ (u"ࠥࡰࡴࡧࡤࡦࡦࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࢁࡩ࡯ࡵࡷࡥࡳࡩࡥ࠯ࡴࡨࡪ࠭࠯ࡽࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࠥᖤ") + str(test_hook_state) + bstack1lll11l_opy_ (u"ࠦࠧᖥ"))
            if test_framework_state == bstack1lll1l11lll_opy_.TEST:
                if test_hook_state == bstack1lll11lll11_opy_.PRE and not TestFramework.bstack1llll11ll11_opy_(instance, TestFramework.bstack1l1lllll111_opy_):
                    TestFramework.bstack1llll1ll11l_opy_(instance, TestFramework.bstack1l1lllll111_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack1lll11l_opy_ (u"ࠧࡹࡥࡵࠢࡷࡩࡸࡺ࠭ࡴࡶࡤࡶࡹࠦࡦࡰࡴࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࢁࡩ࡯ࡵࡷࡥࡳࡩࡥ࠯ࡴࡨࡪ࠭࠯ࡽࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࠥᖦ") + str(test_hook_state) + bstack1lll11l_opy_ (u"ࠨࠢᖧ"))
                elif test_hook_state == bstack1lll11lll11_opy_.POST and not TestFramework.bstack1llll11ll11_opy_(instance, TestFramework.bstack1ll111ll1ll_opy_):
                    TestFramework.bstack1llll1ll11l_opy_(instance, TestFramework.bstack1ll111ll1ll_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack1lll11l_opy_ (u"ࠢࡴࡧࡷࠤࡹ࡫ࡳࡵ࠯ࡨࡲࡩࠦࡦࡰࡴࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࢁࡩ࡯ࡵࡷࡥࡳࡩࡥ࠯ࡴࡨࡪ࠭࠯ࡽࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࠥᖨ") + str(test_hook_state) + bstack1lll11l_opy_ (u"ࠣࠤᖩ"))
            elif test_framework_state == bstack1lll1l11lll_opy_.LOG and test_hook_state == bstack1lll11lll11_opy_.POST:
                bstack1l11lll1lll_opy_.__1l1lll1ll11_opy_(instance, *args)
            elif test_framework_state == bstack1lll1l11lll_opy_.LOG_REPORT and test_hook_state == bstack1lll11lll11_opy_.POST:
                self.__1ll11lll11l_opy_(instance, *args)
                self.__1ll1l111lll_opy_(instance)
            elif test_framework_state in bstack1l11lll1lll_opy_.bstack1ll11ll1lll_opy_:
                self.__1l1lll1ll1l_opy_(instance, test_framework_state, test_hook_state, *args)
            self.logger.debug(bstack1lll11l_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡧࡹࡩࡳࡺ࠺ࠡࡪࡤࡲࡩࡲࡥࡥࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࡿࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࢃࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࠥᖪ") + str(instance.ref()) + bstack1lll11l_opy_ (u"ࠥࠦᖫ"))
        except Exception as e:
            self.logger.error(e)
            traceback.print_exc()
        self.bstack1ll111ll111_opy_(instance, (test_framework_state, test_hook_state), *args, **kwargs)
        try:
            if instance!= None and test_framework_state in bstack1l11lll1lll_opy_.bstack1ll11ll1lll_opy_ and test_hook_state == bstack1lll11lll11_opy_.POST:
                name = str(EVENTS.bstack1ll1l1l111_opy_.name)+bstack1lll11l_opy_ (u"ࠦ࠿ࠨᖬ")+str(test_framework_state.name)
                bstack1ll111111l1_opy_ = TestFramework.bstack1ll11ll1l11_opy_(instance, name)
                bstack1llll1l1l1l_opy_.end(EVENTS.bstack1ll1l1l111_opy_.value, bstack1ll111111l1_opy_+bstack1lll11l_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧᖭ"), bstack1ll111111l1_opy_+bstack1lll11l_opy_ (u"ࠨ࠺ࡦࡰࡧࠦᖮ"), True, None, test_framework_state.name)
        except Exception as e:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡨࡰࡱ࡮ࠤࡪࡸࡲࡰࡴ࠽ࠤࢀࢃࠢᖯ").format(e))
    def bstack1ll1111ll1l_opy_(self):
        return self.bstack1ll1l1l1111_opy_
    def __1ll1111l1l1_opy_(self, *args):
        if len(args) > 2 and callable(getattr(args[2], bstack1lll11l_opy_ (u"ࠣࡩࡨࡸࡤࡸࡥࡴࡷ࡯ࡸࠧᖰ"), None)):
            rep = args[2].get_result()
            if rep:
                return TestFramework.bstack1l1llll1ll1_opy_(rep, [bstack1lll11l_opy_ (u"ࠤࡺ࡬ࡪࡴࠢᖱ"), bstack1lll11l_opy_ (u"ࠥࡳࡺࡺࡣࡰ࡯ࡨࠦᖲ"), bstack1lll11l_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦᖳ"), bstack1lll11l_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧᖴ"), bstack1lll11l_opy_ (u"ࠨࡳ࡬࡫ࡳࡴࡪࡪࠢᖵ"), bstack1lll11l_opy_ (u"ࠢ࡭ࡱࡱ࡫ࡷ࡫ࡰࡳࡶࡨࡼࡹࠨᖶ")])
        return None
    def __1ll11lll11l_opy_(self, instance: bstack1llll111111_opy_, *args):
        result = self.__1ll1111l1l1_opy_(*args)
        if not result:
            return
        failure = None
        bstack1111111lll_opy_ = None
        if result.get(bstack1lll11l_opy_ (u"ࠣࡱࡸࡸࡨࡵ࡭ࡦࠤᖷ"), None) == bstack1lll11l_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤᖸ") and len(args) > 1 and getattr(args[1], bstack1lll11l_opy_ (u"ࠥࡩࡽࡩࡩ࡯ࡨࡲࠦᖹ"), None) is not None:
            failure = [{bstack1lll11l_opy_ (u"ࠫࡧࡧࡣ࡬ࡶࡵࡥࡨ࡫ࠧᖺ"): [args[1].excinfo.exconly(), result.get(bstack1lll11l_opy_ (u"ࠧࡲ࡯࡯ࡩࡵࡩࡵࡸࡴࡦࡺࡷࠦᖻ"), None)]}]
            bstack1111111lll_opy_ = bstack1lll11l_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࡇࡵࡶࡴࡸࠢᖼ") if bstack1lll11l_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࠥᖽ") in getattr(args[1].excinfo, bstack1lll11l_opy_ (u"ࠣࡶࡼࡴࡪࡴࡡ࡮ࡧࠥᖾ"), bstack1lll11l_opy_ (u"ࠤࠥᖿ")) else bstack1lll11l_opy_ (u"࡙ࠥࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࡋࡲࡳࡱࡵࠦᗀ")
        bstack1ll111l1l1l_opy_ = result.get(bstack1lll11l_opy_ (u"ࠦࡴࡻࡴࡤࡱࡰࡩࠧᗁ"), TestFramework.bstack1ll111111ll_opy_)
        if bstack1ll111l1l1l_opy_ != TestFramework.bstack1ll111111ll_opy_:
            TestFramework.bstack1llll1ll11l_opy_(instance, TestFramework.bstack1ll1l11ll11_opy_, datetime.now(tz=timezone.utc))
        TestFramework.bstack1ll11llll11_opy_(instance, {
            TestFramework.bstack1lll11lllll_opy_: failure,
            TestFramework.bstack1ll1111l11l_opy_: bstack1111111lll_opy_,
            TestFramework.bstack1lll1lll11l_opy_: bstack1ll111l1l1l_opy_,
        })
    def __1ll11ll111l_opy_(
        self,
        context: bstack1ll11l1llll_opy_,
        test_framework_state: bstack1lll1l11lll_opy_,
        test_hook_state: bstack1lll11lll11_opy_,
        *args,
        **kwargs,
    ):
        instance = None
        if test_framework_state == bstack1lll1l11lll_opy_.SETUP_FIXTURE:
            instance = self.__1ll1l111l11_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        else:
            target = None # bstack1l1llll1lll_opy_ bstack1ll11111lll_opy_ this to be bstack1lll11l_opy_ (u"ࠧࡴ࡯ࡥࡧ࡬ࡨࠧᗂ")
            if test_framework_state == bstack1lll1l11lll_opy_.INIT_TEST:
                target = args[0] if isinstance(args[0], str) else None
                if target:
                    self.__1ll111lllll_opy_(context, test_framework_state, target, *args)
            elif test_framework_state == bstack1lll1l11lll_opy_.LOG:
                nodeid = getattr(getattr(args[0], bstack1lll11l_opy_ (u"ࠨ࡮ࡰࡦࡨࠦᗃ"), None), bstack1lll11l_opy_ (u"ࠢ࡯ࡱࡧࡩ࡮ࡪࠢᗄ"), None) if args else None
                if isinstance(nodeid, str):
                    target = nodeid
            elif getattr(args[0], bstack1lll11l_opy_ (u"ࠣࡰࡲࡨࡪ࡯ࡤࠣᗅ"), None):
                target = args[0].nodeid
            instance = TestFramework.bstack1ll1l1ll111_opy_(target) if target else None
        return instance
    def __1l1lll1ll1l_opy_(
        self,
        instance: bstack1llll111111_opy_,
        test_framework_state: bstack1lll1l11lll_opy_,
        test_hook_state: bstack1lll11lll11_opy_,
        *args,
    ):
        key = test_framework_state.name
        bstack1ll1l1l11l1_opy_ = TestFramework.get_state(instance, bstack1l11lll1lll_opy_.bstack1ll1l11ll1l_opy_, {})
        if not key in bstack1ll1l1l11l1_opy_:
            bstack1ll1l1l11l1_opy_[key] = []
        bstack1ll111l11ll_opy_ = TestFramework.get_state(instance, bstack1l11lll1lll_opy_.bstack1ll1l11l111_opy_, {})
        if not key in bstack1ll111l11ll_opy_:
            bstack1ll111l11ll_opy_[key] = []
        bstack1ll1l111l1l_opy_ = {
            bstack1l11lll1lll_opy_.bstack1ll1l11ll1l_opy_: bstack1ll1l1l11l1_opy_,
            bstack1l11lll1lll_opy_.bstack1ll1l11l111_opy_: bstack1ll111l11ll_opy_,
        }
        if test_hook_state == bstack1lll11lll11_opy_.PRE:
            hook = {
                bstack1lll11l_opy_ (u"ࠤ࡮ࡩࡾࠨᗆ"): key,
                TestFramework.bstack1ll1l11l1ll_opy_: uuid4().__str__(),
                TestFramework.bstack1l1llll1l1l_opy_: TestFramework.bstack1ll1l1111l1_opy_,
                TestFramework.bstack1ll11l11111_opy_: datetime.now(tz=timezone.utc),
                TestFramework.bstack1ll11l1l11l_opy_: [],
                TestFramework.bstack1l1lllll11l_opy_: args[1] if len(args) > 1 else bstack1lll11l_opy_ (u"ࠪࠫᗇ"),
                TestFramework.bstack1ll111lll1l_opy_: bstack1ll1l1l1ll1_opy_.bstack1ll1111ll11_opy_()
            }
            bstack1ll1l1l11l1_opy_[key].append(hook)
            bstack1ll1l111l1l_opy_[bstack1l11lll1lll_opy_.bstack1l1lllllll1_opy_] = key
        elif test_hook_state == bstack1lll11lll11_opy_.POST:
            bstack1ll111l11l1_opy_ = bstack1ll1l1l11l1_opy_.get(key, [])
            hook = bstack1ll111l11l1_opy_.pop() if bstack1ll111l11l1_opy_ else None
            if hook:
                result = self.__1ll1111l1l1_opy_(*args)
                if result:
                    bstack1ll11l1ll1l_opy_ = result.get(bstack1lll11l_opy_ (u"ࠦࡴࡻࡴࡤࡱࡰࡩࠧᗈ"), TestFramework.bstack1ll1l1111l1_opy_)
                    if bstack1ll11l1ll1l_opy_ != TestFramework.bstack1ll1l1111l1_opy_:
                        hook[TestFramework.bstack1l1llll1l1l_opy_] = bstack1ll11l1ll1l_opy_
                hook[TestFramework.bstack1ll11llll1l_opy_] = datetime.now(tz=timezone.utc)
                hook[TestFramework.bstack1ll111lll1l_opy_]= bstack1ll1l1l1ll1_opy_.bstack1ll1111ll11_opy_()
                self.bstack1l1llll111l_opy_(hook)
                logs = hook.get(TestFramework.bstack1ll1l1l1l11_opy_, [])
                if logs: self.bstack1ll1l11l1l1_opy_(instance, logs)
                bstack1ll111l11ll_opy_[key].append(hook)
                bstack1ll1l111l1l_opy_[bstack1l11lll1lll_opy_.bstack1ll111l111l_opy_] = key
        TestFramework.bstack1ll11llll11_opy_(instance, bstack1ll1l111l1l_opy_)
        self.logger.debug(bstack1lll11l_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣ࡭ࡵ࡯࡬ࡡࡨࡺࡪࡴࡴ࠻ࠢࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࡁࢀࡱࡥࡺࡿ࠱ࡿࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࢃࠠࡩࡱࡲ࡯ࡸࡥࡳࡵࡣࡵࡸࡪࡪ࠽ࡼࡪࡲࡳࡰࡹ࡟ࡴࡶࡤࡶࡹ࡫ࡤࡾࠢ࡫ࡳࡴࡱࡳࡠࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡀࠦᗉ") + str(bstack1ll111l11ll_opy_) + bstack1lll11l_opy_ (u"ࠨࠢᗊ"))
    def __1ll1l111l11_opy_(
        self,
        context: bstack1ll11l1llll_opy_,
        test_framework_state: bstack1lll1l11lll_opy_,
        test_hook_state: bstack1lll11lll11_opy_,
        *args,
        **kwargs,
    ):
        fixturedef = TestFramework.bstack1l1llll1ll1_opy_(args[0], [bstack1lll11l_opy_ (u"ࠢࡴࡥࡲࡴࡪࠨᗋ"), bstack1lll11l_opy_ (u"ࠣࡣࡵ࡫ࡳࡧ࡭ࡦࠤᗌ"), bstack1lll11l_opy_ (u"ࠤࡳࡥࡷࡧ࡭ࡴࠤᗍ"), bstack1lll11l_opy_ (u"ࠥ࡭ࡩࡹࠢᗎ"), bstack1lll11l_opy_ (u"ࠦࡺࡴࡩࡵࡶࡨࡷࡹࠨᗏ"), bstack1lll11l_opy_ (u"ࠧࡨࡡࡴࡧ࡬ࡨࠧᗐ")]) if len(args) > 0 else {}
        request = args[1] if len(args) > 1 else None
        scope = request.scope if hasattr(request, bstack1lll11l_opy_ (u"ࠨࡳࡤࡱࡳࡩࠧᗑ")) else fixturedef.get(bstack1lll11l_opy_ (u"ࠢࡴࡥࡲࡴࡪࠨᗒ"), None)
        fixturename = request.fixturename if hasattr(request, bstack1lll11l_opy_ (u"ࠣࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࠨᗓ")) else None
        node = request.node if hasattr(request, bstack1lll11l_opy_ (u"ࠤࡱࡳࡩ࡫ࠢᗔ")) else None
        target = request.node.nodeid if hasattr(node, bstack1lll11l_opy_ (u"ࠥࡲࡴࡪࡥࡪࡦࠥᗕ")) else None
        baseid = fixturedef.get(bstack1lll11l_opy_ (u"ࠦࡧࡧࡳࡦ࡫ࡧࠦᗖ"), None) or bstack1lll11l_opy_ (u"ࠧࠨᗗ")
        if (not target or len(baseid) > 0) and hasattr(request, bstack1lll11l_opy_ (u"ࠨ࡟ࡱࡻࡩࡹࡳࡩࡩࡵࡧࡰࠦᗘ")):
            target = bstack1l11lll1lll_opy_.__1ll11l1l111_opy_(request._pyfuncitem.location) if hasattr(request._pyfuncitem, bstack1lll11l_opy_ (u"ࠢ࡭ࡱࡦࡥࡹ࡯࡯࡯ࠤᗙ")) else None
            if target and not TestFramework.bstack1ll1l1ll111_opy_(target):
                self.__1ll111lllll_opy_(context, test_framework_state, target, (target, request._pyfuncitem.location))
                node = request._pyfuncitem
                self.logger.debug(bstack1lll11l_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡠࡧࡹࡩࡳࡺ࠺ࠡࡨࡤࡰࡱࡨࡡࡤ࡭ࠣࡸࡦࡸࡧࡦࡶࡀࡿࡹࡧࡲࡨࡧࡷࢁࠥ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࡀࡿ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦࡿࠣࡲࡴࡪࡥ࠾ࡽࡱࡳࡩ࡫ࡽࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࠥᗚ") + str(test_hook_state) + bstack1lll11l_opy_ (u"ࠤࠥᗛ"))
        if not fixturedef or not scope or not target:
            self.logger.warning(bstack1lll11l_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡩ࡭ࡽࡺࡵࡳࡧࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡹࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࡼࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࢀࠤ࡫࡯ࡸࡵࡷࡵࡩࡩ࡫ࡦ࠾ࡽࡩ࡭ࡽࡺࡵࡳࡧࡧࡩ࡫ࢃࠠࡴࡥࡲࡴࡪࡃࡻࡴࡥࡲࡴࡪࢃࠠࡵࡣࡵ࡫ࡪࡺ࠽ࠣᗜ") + str(target) + bstack1lll11l_opy_ (u"ࠦࠧᗝ"))
            return None
        instance = TestFramework.bstack1ll1l1ll111_opy_(target)
        if not instance:
            self.logger.warning(bstack1lll11l_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣ࡫࡯ࡸࡵࡷࡵࡩࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡻ࡮ࡩࡣࡱࡨࡱ࡫ࡤࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࡾࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࢂࠦࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࡁࢀ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࢀࠤࡸࡩ࡯ࡱࡧࡀࡿࡸࡩ࡯ࡱࡧࢀࠤࡧࡧࡳࡦ࡫ࡧࡁࢀࡨࡡࡴࡧ࡬ࡨࢂࠦࡴࡢࡴࡪࡩࡹࡃࠢᗞ") + str(target) + bstack1lll11l_opy_ (u"ࠨࠢᗟ"))
            return None
        bstack1l1llll1111_opy_ = TestFramework.get_state(instance, bstack1l11lll1lll_opy_.bstack1ll11lll111_opy_, {})
        if os.getenv(bstack1lll11l_opy_ (u"ࠢࡔࡆࡎࡣࡈࡒࡉࡠࡈࡏࡅࡌࡥࡆࡊ࡚ࡗ࡙ࡗࡋࡓࠣᗠ"), bstack1lll11l_opy_ (u"ࠣ࠳ࠥᗡ")) == bstack1lll11l_opy_ (u"ࠤ࠴ࠦᗢ"):
            bstack1ll11l1lll1_opy_ = bstack1lll11l_opy_ (u"ࠥ࠾ࠧᗣ").join((scope, fixturename))
            bstack1ll111l1l11_opy_ = datetime.now(tz=timezone.utc)
            bstack1ll11l111l1_opy_ = {
                bstack1lll11l_opy_ (u"ࠦࡰ࡫ࡹࠣᗤ"): bstack1ll11l1lll1_opy_,
                bstack1lll11l_opy_ (u"ࠧࡺࡡࡨࡵࠥᗥ"): bstack1l11lll1lll_opy_.__1ll1111lll1_opy_(request.node),
                bstack1lll11l_opy_ (u"ࠨࡦࡪࡺࡷࡹࡷ࡫ࠢᗦ"): fixturedef,
                bstack1lll11l_opy_ (u"ࠢࡴࡥࡲࡴࡪࠨᗧ"): scope,
                bstack1lll11l_opy_ (u"ࠣࡶࡼࡴࡪࠨᗨ"): None,
            }
            try:
                if test_hook_state == bstack1lll11lll11_opy_.POST and callable(getattr(args[-1], bstack1lll11l_opy_ (u"ࠤࡪࡩࡹࡥࡲࡦࡵࡸࡰࡹࠨᗩ"), None)):
                    bstack1ll11l111l1_opy_[bstack1lll11l_opy_ (u"ࠥࡸࡾࡶࡥࠣᗪ")] = TestFramework.bstack1ll1111l1ll_opy_(args[-1].get_result())
            except Exception as e:
                pass
            if test_hook_state == bstack1lll11lll11_opy_.PRE:
                bstack1ll11l111l1_opy_[bstack1lll11l_opy_ (u"ࠦࡺࡻࡩࡥࠤᗫ")] = uuid4().__str__()
                bstack1ll11l111l1_opy_[bstack1l11lll1lll_opy_.bstack1ll11l11111_opy_] = bstack1ll111l1l11_opy_
            elif test_hook_state == bstack1lll11lll11_opy_.POST:
                bstack1ll11l111l1_opy_[bstack1l11lll1lll_opy_.bstack1ll11llll1l_opy_] = bstack1ll111l1l11_opy_
            if bstack1ll11l1lll1_opy_ in bstack1l1llll1111_opy_:
                bstack1l1llll1111_opy_[bstack1ll11l1lll1_opy_].update(bstack1ll11l111l1_opy_)
                self.logger.debug(bstack1lll11l_opy_ (u"ࠧࡻࡰࡥࡣࡷࡩࡩࠦࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࡁࢀ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࢀࠤࡸࡩ࡯ࡱࡧࡀࡿࡸࡩ࡯ࡱࡧࢀࠤ࡫࡯ࡸࡵࡷࡵࡩࡂࠨᗬ") + str(bstack1l1llll1111_opy_[bstack1ll11l1lll1_opy_]) + bstack1lll11l_opy_ (u"ࠨࠢᗭ"))
            else:
                bstack1l1llll1111_opy_[bstack1ll11l1lll1_opy_] = bstack1ll11l111l1_opy_
                self.logger.debug(bstack1lll11l_opy_ (u"ࠢࡴࡣࡹࡩࡩࠦࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࡁࢀ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࢀࠤࡸࡩ࡯ࡱࡧࡀࡿࡸࡩ࡯ࡱࡧࢀࠤ࡫࡯ࡸࡵࡷࡵࡩࡂࢁࡴࡦࡵࡷࡣ࡫࡯ࡸࡵࡷࡵࡩࢂࠦࡴࡳࡣࡦ࡯ࡪࡪ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡴ࠿ࠥᗮ") + str(len(bstack1l1llll1111_opy_)) + bstack1lll11l_opy_ (u"ࠣࠤᗯ"))
        TestFramework.bstack1llll1ll11l_opy_(instance, bstack1l11lll1lll_opy_.bstack1ll11lll111_opy_, bstack1l1llll1111_opy_)
        self.logger.debug(bstack1lll11l_opy_ (u"ࠤࡶࡥࡻ࡫ࡤࠡࡨ࡬ࡼࡹࡻࡲࡦࡵࡀࡿࡱ࡫࡮ࠩࡶࡵࡥࡨࡱࡥࡥࡡࡩ࡭ࡽࡺࡵࡳࡧࡶ࠭ࢂࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࠤᗰ") + str(instance.ref()) + bstack1lll11l_opy_ (u"ࠥࠦᗱ"))
        return instance
    def __1ll111lllll_opy_(
        self,
        context: bstack1ll11l1llll_opy_,
        test_framework_state: bstack1lll1l11lll_opy_,
        target: Any,
        *args,
    ):
        ctx = bstack1ll1ll11l1l_opy_.create_context(target)
        ob = bstack1llll111111_opy_(ctx, self.bstack1l1llllll11_opy_, self.bstack1ll111llll1_opy_, test_framework_state)
        TestFramework.bstack1ll11llll11_opy_(ob, {
            TestFramework.bstack1llll1111l1_opy_: context.test_framework_name,
            TestFramework.bstack1lll1l1l111_opy_: context.test_framework_version,
            TestFramework.bstack1ll11l1ll11_opy_: [],
            bstack1l11lll1lll_opy_.bstack1ll11lll111_opy_: {},
            bstack1l11lll1lll_opy_.bstack1ll1l11l111_opy_: {},
            bstack1l11lll1lll_opy_.bstack1ll1l11ll1l_opy_: {},
        })
        if len(args) > 1 and isinstance(args[1], tuple):
            TestFramework.bstack1llll1ll11l_opy_(ob, TestFramework.bstack1ll111ll1l1_opy_, str(args[1][0]))
        if context.platform_index >= 0:
            TestFramework.bstack1llll1ll11l_opy_(ob, TestFramework.bstack1lllllllll1_opy_, context.platform_index)
        TestFramework.bstack1llll111ll1_opy_[ctx.id] = ob
        self.logger.debug(bstack1lll11l_opy_ (u"ࠦࡸࡧࡶࡦࡦࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࠥࡩࡴࡹ࠰࡬ࡨࡂࢁࡣࡵࡺ࠱࡭ࡩࢃࠠࡵࡣࡵ࡫ࡪࡺ࠽ࡼࡶࡤࡶ࡬࡫ࡴࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠࡪࡰࡶࡸࡦࡴࡣࡦࡵࡀࠦᗲ") + str(TestFramework.bstack1llll111ll1_opy_.keys()) + bstack1lll11l_opy_ (u"ࠧࠨᗳ"))
        return ob
    def bstack1ll1l11l11l_opy_(self, instance: bstack1llll111111_opy_, bstack1lllll1l111_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1lll11lll11_opy_]):
        bstack1ll111ll11l_opy_ = (
            bstack1l11lll1lll_opy_.bstack1l1lllllll1_opy_
            if bstack1lllll1l111_opy_[1] == bstack1lll11lll11_opy_.PRE
            else bstack1l11lll1lll_opy_.bstack1ll111l111l_opy_
        )
        hook = bstack1l11lll1lll_opy_.bstack1ll11ll11ll_opy_(instance, bstack1ll111ll11l_opy_)
        entries = hook.get(TestFramework.bstack1ll11l1l11l_opy_, []) if isinstance(hook, dict) else []
        entries.extend(TestFramework.get_state(instance, TestFramework.bstack1ll11l1ll11_opy_, []))
        return entries
    def bstack1ll11l11l11_opy_(self, instance: bstack1llll111111_opy_, bstack1lllll1l111_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1lll11lll11_opy_]):
        bstack1ll111ll11l_opy_ = (
            bstack1l11lll1lll_opy_.bstack1l1lllllll1_opy_
            if bstack1lllll1l111_opy_[1] == bstack1lll11lll11_opy_.PRE
            else bstack1l11lll1lll_opy_.bstack1ll111l111l_opy_
        )
        bstack1l11lll1lll_opy_.bstack1ll11ll1111_opy_(instance, bstack1ll111ll11l_opy_)
        TestFramework.get_state(instance, TestFramework.bstack1ll11l1ll11_opy_, []).clear()
    def bstack1l1llll111l_opy_(self, hook: Dict[str, Any]) -> None:
        bstack1lll11l_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡔࡷࡵࡣࡦࡵࡶࡩࡸࠦࡴࡩࡧࠣࡌࡴࡵ࡫ࡍࡧࡹࡩࡱࠦࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࡶࠤࡸ࡯࡭ࡪ࡮ࡤࡶࠥࡺ࡯ࠡࡶ࡫ࡩࠥࡐࡡࡷࡣࠣ࡭ࡲࡶ࡬ࡦ࡯ࡨࡲࡹࡧࡴࡪࡱࡱ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡔࡩ࡫ࡶࠤࡲ࡫ࡴࡩࡱࡧ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡇ࡭࡫ࡣ࡬ࡵࠣࡸ࡭࡫ࠠࡉࡱࡲ࡯ࡑ࡫ࡶࡦ࡮ࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠦࡩ࡯ࡵ࡬ࡨࡪࠦࡾ࠰࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠰ࡗࡳࡰࡴࡧࡤࡦࡦࡄࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࡹ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡆࡰࡴࠣࡩࡦࡩࡨࠡࡨ࡬ࡰࡪࠦࡩ࡯ࠢ࡫ࡳࡴࡱ࡟࡭ࡧࡹࡩࡱࡥࡦࡪ࡮ࡨࡷ࠱ࠦࡲࡦࡲ࡯ࡥࡨ࡫ࡳࠡࠤࡗࡩࡸࡺࡌࡦࡸࡨࡰࠧࠦࡷࡪࡶ࡫ࠤࠧࡎ࡯ࡰ࡭ࡏࡩࡻ࡫࡬ࠣࠢ࡬ࡲࠥ࡯ࡴࡴࠢࡳࡥࡹ࡮࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡉࡧࠢࡤࠤ࡫࡯࡬ࡦࠢ࡬ࡲࠥࡺࡨࡦࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥࡳࡡࡵࡥ࡫ࡩࡸࠦࡡࠡ࡯ࡲࡨ࡮࡬ࡩࡦࡦࠣ࡬ࡴࡵ࡫࠮࡮ࡨࡺࡪࡲࠠࡧ࡫࡯ࡩ࠱ࠦࡩࡵࠢࡦࡶࡪࡧࡴࡦࡵࠣࡥࠥࡒ࡯ࡨࡇࡱࡸࡷࡿࠠࡰࡤ࡭ࡩࡨࡺࠠࡸ࡫ࡷ࡬ࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࠢࡧࡩࡹࡧࡩ࡭ࡵ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡖ࡭ࡲ࡯࡬ࡢࡴ࡯ࡽ࠱ࠦࡩࡵࠢࡳࡶࡴࡩࡥࡴࡵࡨࡷࠥࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࠢࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࡹࠠ࡭ࡱࡦࡥࡹ࡫ࡤࠡ࡫ࡱࠤࡍࡵ࡯࡬ࡎࡨࡺࡪࡲ࠯ࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࡌࡴࡵ࡫ࡆࡸࡨࡲࡹࠦࡢࡺࠢࡵࡩࡵࡲࡡࡤ࡫ࡱ࡫ࠥࠨࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࠥࠤࡼ࡯ࡴࡩࠢࠥࡌࡴࡵ࡫ࡍࡧࡹࡩࡱ࠵ࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࡋࡳࡴࡱࡅࡷࡧࡱࡸࠧ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱࡚ࠥࡨࡦࠢࡦࡶࡪࡧࡴࡦࡦࠣࡐࡴ࡭ࡅ࡯ࡶࡵࡽࠥࡵࡢ࡫ࡧࡦࡸࡸࠦࡡࡳࡧࠣࡥࡩࡪࡥࡥࠢࡷࡳࠥࡺࡨࡦࠢ࡫ࡳࡴࡱࠧࡴࠢࠥࡰࡴ࡭ࡳࠣࠢ࡯࡭ࡸࡺ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡄࡶ࡬ࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡨࡰࡱ࡮࠾࡚ࠥࡨࡦࠢࡨࡺࡪࡴࡴࠡࡦ࡬ࡧࡹ࡯࡯࡯ࡣࡵࡽࠥࡩ࡯࡯ࡶࡤ࡭ࡳ࡯࡮ࡨࠢࡨࡼ࡮ࡹࡴࡪࡰࡪࠤࡱࡵࡧࡴࠢࡤࡲࡩࠦࡨࡰࡱ࡮ࠤ࡮ࡴࡦࡰࡴࡰࡥࡹ࡯࡯࡯࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡪࡲࡳࡰࡥ࡬ࡦࡸࡨࡰࡤ࡬ࡩ࡭ࡧࡶ࠾ࠥࡒࡩࡴࡶࠣࡳ࡫ࠦࡐࡢࡶ࡫ࠤࡴࡨࡪࡦࡥࡷࡷࠥ࡬ࡲࡰ࡯ࠣࡸ࡭࡫ࠠࡕࡧࡶࡸࡑ࡫ࡶࡦ࡮ࠣࡱࡴࡴࡩࡵࡱࡵ࡭ࡳ࡭࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡢࡶ࡫࡯ࡨࡤࡲࡥࡷࡧ࡯ࡣ࡫࡯࡬ࡦࡵ࠽ࠤࡑ࡯ࡳࡵࠢࡲࡪࠥࡖࡡࡵࡪࠣࡳࡧࡰࡥࡤࡶࡶࠤ࡫ࡸ࡯࡮ࠢࡷ࡬ࡪࠦࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࠣࡱࡴࡴࡩࡵࡱࡵ࡭ࡳ࡭࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧᗴ")
        global _1ll111l1111_opy_
        platform_index = os.environ[bstack1lll11l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧᗵ")]
        bstack1ll11lllll1_opy_ = os.path.join(bstack1ll1l11lll1_opy_, (bstack1ll11ll1l1l_opy_ + str(platform_index)), bstack11lll1lll11_opy_)
        if not os.path.exists(bstack1ll11lllll1_opy_) or not os.path.isdir(bstack1ll11lllll1_opy_):
            self.logger.debug(bstack1lll11l_opy_ (u"ࠣࡆ࡬ࡶࡪࡩࡴࡰࡴࡼࠤࡩࡵࡥࡴࠢࡱࡳࡹࠦࡥࡹ࡫ࡶࡸࡸࠦࡴࡰࠢࡳࡶࡴࡩࡥࡴࡵࠣࡿࢂࠨᗶ").format(bstack1ll11lllll1_opy_))
            return
        logs = hook.get(bstack1lll11l_opy_ (u"ࠤ࡯ࡳ࡬ࡹࠢᗷ"), [])
        with os.scandir(bstack1ll11lllll1_opy_) as entries:
            for entry in entries:
                abs_path = os.path.abspath(entry.path)
                if abs_path in _1ll111l1111_opy_:
                    self.logger.info(bstack1lll11l_opy_ (u"ࠥࡔࡦࡺࡨࠡࡣ࡯ࡶࡪࡧࡤࡺࠢࡳࡶࡴࡩࡥࡴࡵࡨࡨࠥࢁࡽࠣᗸ").format(abs_path))
                    continue
                if entry.is_file():
                    try:
                        timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                    except Exception:
                        timestamp = bstack1lll11l_opy_ (u"ࠦࠧᗹ")
                    log_entry = bstack1l1lllll1ll_opy_(
                        kind=bstack1lll11l_opy_ (u"࡚ࠧࡅࡔࡖࡢࡅ࡙࡚ࡁࡄࡊࡐࡉࡓ࡚ࠢᗺ"),
                        message=bstack1lll11l_opy_ (u"ࠨࠢᗻ"),
                        level=bstack1lll11l_opy_ (u"ࠢࠣᗼ"),
                        timestamp=timestamp,
                        fileName=entry.name,
                        bstack1ll11111l1l_opy_=entry.stat().st_size,
                        bstack1ll1l1l111l_opy_=bstack1lll11l_opy_ (u"ࠣࡏࡄࡒ࡚ࡇࡌࡠࡗࡓࡐࡔࡇࡄࠣᗽ"),
                        bstack1ll111l_opy_=os.path.abspath(entry.path),
                        bstack1ll1l11111l_opy_=hook.get(TestFramework.bstack1ll1l11l1ll_opy_)
                    )
                    logs.append(log_entry)
                    _1ll111l1111_opy_.add(abs_path)
        platform_index = os.environ[bstack1lll11l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩᗾ")]
        bstack1ll111l1lll_opy_ = os.path.join(bstack1ll1l11lll1_opy_, (bstack1ll11ll1l1l_opy_ + str(platform_index)), bstack11lll1lll11_opy_, bstack11lll1ll1ll_opy_)
        if not os.path.exists(bstack1ll111l1lll_opy_) or not os.path.isdir(bstack1ll111l1lll_opy_):
            self.logger.info(bstack1lll11l_opy_ (u"ࠥࡒࡴࠦࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࡋࡳࡴࡱࡅࡷࡧࡱࡸࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠦࡦࡰࡷࡱࡨࠥࡧࡴ࠻ࠢࡾࢁࠧᗿ").format(bstack1ll111l1lll_opy_))
        else:
            self.logger.info(bstack1lll11l_opy_ (u"ࠦࡕࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࡍࡵ࡯࡬ࡇࡹࡩࡳࡺࠠࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷࠥ࡬ࡲࡰ࡯ࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࡀࠠࡼࡿࠥᘀ").format(bstack1ll111l1lll_opy_))
            with os.scandir(bstack1ll111l1lll_opy_) as entries:
                for entry in entries:
                    abs_path = os.path.abspath(entry.path)
                    if abs_path in _1ll111l1111_opy_:
                        self.logger.info(bstack1lll11l_opy_ (u"ࠧࡖࡡࡵࡪࠣࡥࡱࡸࡥࡢࡦࡼࠤࡵࡸ࡯ࡤࡧࡶࡷࡪࡪࠠࡼࡿࠥᘁ").format(abs_path))
                        continue
                    if entry.is_file():
                        try:
                            timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                        except Exception:
                            timestamp = bstack1lll11l_opy_ (u"ࠨࠢᘂ")
                        log_entry = bstack1l1lllll1ll_opy_(
                            kind=bstack1lll11l_opy_ (u"ࠢࡕࡇࡖࡘࡤࡇࡔࡕࡃࡆࡌࡒࡋࡎࡕࠤᘃ"),
                            message=bstack1lll11l_opy_ (u"ࠣࠤᘄ"),
                            level=bstack1lll11l_opy_ (u"ࠤࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࠨᘅ"),
                            timestamp=timestamp,
                            fileName=entry.name,
                            bstack1ll11111l1l_opy_=entry.stat().st_size,
                            bstack1ll1l1l111l_opy_=bstack1lll11l_opy_ (u"ࠥࡑࡆࡔࡕࡂࡎࡢ࡙ࡕࡒࡏࡂࡆࠥᘆ"),
                            bstack1ll111l_opy_=os.path.abspath(entry.path),
                            bstack1ll1l1l1lll_opy_=hook.get(TestFramework.bstack1ll1l11l1ll_opy_)
                        )
                        logs.append(log_entry)
                        _1ll111l1111_opy_.add(abs_path)
        hook[bstack1lll11l_opy_ (u"ࠦࡱࡵࡧࡴࠤᘇ")] = logs
    def bstack1ll1l11l1l1_opy_(
        self,
        bstack1ll1l11llll_opy_: bstack1llll111111_opy_,
        entries: List[bstack1l1lllll1ll_opy_],
    ):
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = os.environ.get(bstack1lll11l_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡒࡉࡠࡄࡌࡒࡤ࡙ࡅࡔࡕࡌࡓࡓࡥࡉࡅࠤᘈ"))
        req.platform_index = TestFramework.get_state(bstack1ll1l11llll_opy_, TestFramework.bstack1lllllllll1_opy_)
        req.execution_context.hash = str(bstack1ll1l11llll_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll1l11llll_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll1l11llll_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1ll1l11llll_opy_, TestFramework.bstack1llll1111l1_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1ll1l11llll_opy_, TestFramework.bstack1lll1l1l111_opy_)
            log_entry.uuid = entry.bstack1ll1l11111l_opy_
            log_entry.test_framework_state = bstack1ll1l11llll_opy_.state.name
            log_entry.message = entry.message.encode(bstack1lll11l_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧᘉ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            log_entry.level = bstack1lll11l_opy_ (u"ࠢࠣᘊ")
            if entry.kind == bstack1lll11l_opy_ (u"ࠣࡖࡈࡗ࡙ࡥࡁࡕࡖࡄࡇࡍࡓࡅࡏࡖࠥᘋ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1ll11111l1l_opy_
                log_entry.file_path = entry.bstack1ll111l_opy_
        def bstack1l1llll1l11_opy_():
            bstack11ll11l1l_opy_ = datetime.now()
            try:
                self.bstack1llll11l11l_opy_.LogCreatedEvent(req)
                bstack1ll1l11llll_opy_.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡴࡧࡱࡨࡤࡲ࡯ࡨࡡࡦࡶࡪࡧࡴࡦࡦࡢࡩࡻ࡫࡮ࡵࡡࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࠨᘌ"), datetime.now() - bstack11ll11l1l_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack1lll11l_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࡴࡧࡱࡨࡤࡲ࡯ࡨࡡࡦࡶࡪࡧࡴࡦࡦࡢࡩࡻ࡫࡮ࡵࡡࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࠦࡻࡾࠤᘍ").format(str(e)))
                traceback.print_exc()
        self.bstack1lll11l1l1l_opy_.enqueue(bstack1l1llll1l11_opy_)
    def __1ll1l111lll_opy_(self, instance) -> None:
        bstack1lll11l_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡎࡲࡥࡩࡹࠠࡤࡷࡶࡸࡴࡳࠠࡵࡣࡪࡷࠥ࡬࡯ࡳࠢࡷ࡬ࡪࠦࡧࡪࡸࡨࡲࠥࡺࡥࡴࡶࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡇࡷ࡫ࡡࡵࡧࡶࠤࡦࠦࡤࡪࡥࡷࠤࡨࡵ࡮ࡵࡣ࡬ࡲ࡮ࡴࡧࠡࡶࡨࡷࡹࠦ࡬ࡦࡸࡨࡰࠥࡩࡵࡴࡶࡲࡱࠥࡳࡥࡵࡣࡧࡥࡹࡧࠠࡳࡧࡷࡶ࡮࡫ࡶࡦࡦࠣࡪࡷࡵ࡭ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡆࡹࡸࡺ࡯࡮ࡖࡤ࡫ࡒࡧ࡮ࡢࡩࡨࡶࠥࡧ࡮ࡥࠢࡸࡴࡩࡧࡴࡦࡵࠣࡸ࡭࡫ࠠࡪࡰࡶࡸࡦࡴࡣࡦࠢࡶࡸࡦࡺࡥࠡࡷࡶ࡭ࡳ࡭ࠠࡴࡧࡷࡣࡸࡺࡡࡵࡧࡢࡩࡳࡺࡲࡪࡧࡶ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤᘎ")
        bstack1ll1l111l1l_opy_ = {bstack1lll11l_opy_ (u"ࠧࡩࡵࡴࡶࡲࡱࡤࡳࡥࡵࡣࡧࡥࡹࡧࠢᘏ"): bstack1ll1l1l1ll1_opy_.bstack1ll1111ll11_opy_()}
        from browserstack_sdk.sdk_cli.test_framework import TestFramework
        TestFramework.bstack1ll11llll11_opy_(instance, bstack1ll1l111l1l_opy_)
    @staticmethod
    def bstack1ll11ll11ll_opy_(instance: bstack1llll111111_opy_, bstack1ll111ll11l_opy_: str):
        bstack1ll1111llll_opy_ = (
            bstack1l11lll1lll_opy_.bstack1ll1l11l111_opy_
            if bstack1ll111ll11l_opy_ == bstack1l11lll1lll_opy_.bstack1ll111l111l_opy_
            else bstack1l11lll1lll_opy_.bstack1ll1l11ll1l_opy_
        )
        bstack1l1llll11l1_opy_ = TestFramework.get_state(instance, bstack1ll111ll11l_opy_, None)
        bstack1ll11llllll_opy_ = TestFramework.get_state(instance, bstack1ll1111llll_opy_, None) if bstack1l1llll11l1_opy_ else None
        return (
            bstack1ll11llllll_opy_[bstack1l1llll11l1_opy_][-1]
            if isinstance(bstack1ll11llllll_opy_, dict) and len(bstack1ll11llllll_opy_.get(bstack1l1llll11l1_opy_, [])) > 0
            else None
        )
    @staticmethod
    def bstack1ll11ll1111_opy_(instance: bstack1llll111111_opy_, bstack1ll111ll11l_opy_: str):
        hook = bstack1l11lll1lll_opy_.bstack1ll11ll11ll_opy_(instance, bstack1ll111ll11l_opy_)
        if isinstance(hook, dict):
            hook.get(TestFramework.bstack1ll11l1l11l_opy_, []).clear()
    @staticmethod
    def __1l1lll1ll11_opy_(instance: bstack1llll111111_opy_, *args):
        if len(args) < 2 or not callable(getattr(args[1], bstack1lll11l_opy_ (u"ࠨࡧࡦࡶࡢࡶࡪࡩ࡯ࡳࡦࡶࠦᘐ"), None)):
            return
        if os.getenv(bstack1lll11l_opy_ (u"ࠢࡔࡆࡎࡣࡈࡒࡉࡠࡈࡏࡅࡌࡥࡌࡐࡉࡖࠦᘑ"), bstack1lll11l_opy_ (u"ࠣ࠳ࠥᘒ")) != bstack1lll11l_opy_ (u"ࠤ࠴ࠦᘓ"):
            bstack1l11lll1lll_opy_.logger.warning(bstack1lll11l_opy_ (u"ࠥ࡭࡬ࡴ࡯ࡳ࡫ࡱ࡫ࠥࡩࡡࡱ࡮ࡲ࡫ࠧᘔ"))
            return
        bstack1l1llll11ll_opy_ = {
            bstack1lll11l_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࠥᘕ"): (bstack1l11lll1lll_opy_.bstack1l1lllllll1_opy_, bstack1l11lll1lll_opy_.bstack1ll1l11ll1l_opy_),
            bstack1lll11l_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴࠢᘖ"): (bstack1l11lll1lll_opy_.bstack1ll111l111l_opy_, bstack1l11lll1lll_opy_.bstack1ll1l11l111_opy_),
        }
        for when in (bstack1lll11l_opy_ (u"ࠨࡳࡦࡶࡸࡴࠧᘗ"), bstack1lll11l_opy_ (u"ࠢࡤࡣ࡯ࡰࠧᘘ"), bstack1lll11l_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࠥᘙ")):
            bstack1ll11111111_opy_ = args[1].get_records(when)
            if not bstack1ll11111111_opy_:
                continue
            records = [
                bstack1l1lllll1ll_opy_(
                    kind=TestFramework.bstack1l1lllll1l1_opy_,
                    message=r.message,
                    level=r.levelname if hasattr(r, bstack1lll11l_opy_ (u"ࠤ࡯ࡩࡻ࡫࡬࡯ࡣࡰࡩࠧᘚ")) and r.levelname else None,
                    timestamp=(
                        datetime.fromtimestamp(r.created, tz=timezone.utc)
                        if hasattr(r, bstack1lll11l_opy_ (u"ࠥࡧࡷ࡫ࡡࡵࡧࡧࠦᘛ")) and r.created
                        else None
                    ),
                )
                for r in bstack1ll11111111_opy_
                if isinstance(getattr(r, bstack1lll11l_opy_ (u"ࠦࡲ࡫ࡳࡴࡣࡪࡩࠧᘜ"), None), str) and r.message.strip()
            ]
            if not records:
                continue
            bstack1ll11l11l1l_opy_, bstack1ll1111llll_opy_ = bstack1l1llll11ll_opy_.get(when, (None, None))
            bstack1ll11l1l1ll_opy_ = TestFramework.get_state(instance, bstack1ll11l11l1l_opy_, None) if bstack1ll11l11l1l_opy_ else None
            bstack1ll11llllll_opy_ = TestFramework.get_state(instance, bstack1ll1111llll_opy_, None) if bstack1ll11l1l1ll_opy_ else None
            if isinstance(bstack1ll11llllll_opy_, dict) and len(bstack1ll11llllll_opy_.get(bstack1ll11l1l1ll_opy_, [])) > 0:
                hook = bstack1ll11llllll_opy_[bstack1ll11l1l1ll_opy_][-1]
                if isinstance(hook, dict) and TestFramework.bstack1ll11l1l11l_opy_ in hook:
                    hook[TestFramework.bstack1ll11l1l11l_opy_].extend(records)
                    continue
            logs = TestFramework.get_state(instance, TestFramework.bstack1ll11l1ll11_opy_, [])
            logs.extend(records)
    @staticmethod
    def __1ll11lll1ll_opy_(test) -> Dict[str, Any]:
        test_id = bstack1l11lll1lll_opy_.__1ll11l1l111_opy_(test.location) if hasattr(test, bstack1lll11l_opy_ (u"ࠧࡲ࡯ࡤࡣࡷ࡭ࡴࡴࠢᘝ")) else getattr(test, bstack1lll11l_opy_ (u"ࠨ࡮ࡰࡦࡨ࡭ࡩࠨᘞ"), None)
        test_name = test.name if hasattr(test, bstack1lll11l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᘟ")) else None
        bstack1ll1l1ll11l_opy_ = test.fspath.strpath if hasattr(test, bstack1lll11l_opy_ (u"ࠣࡨࡶࡴࡦࡺࡨࠣᘠ")) and test.fspath else None
        if not test_id or not test_name or not bstack1ll1l1ll11l_opy_:
            return None
        code = None
        if hasattr(test, bstack1lll11l_opy_ (u"ࠤࡲࡦ࡯ࠨᘡ")):
            try:
                import inspect
                code = inspect.getsource(test.obj)
            except:
                pass
        bstack11lll1lllll_opy_ = []
        try:
            bstack11lll1lllll_opy_ = bstack1l11111l_opy_.bstack1lll1lll_opy_(test)
        except:
            bstack1l11lll1lll_opy_.logger.warning(bstack1lll11l_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡦࡪࡰࡧࠤࡹ࡫ࡳࡵࠢࡶࡧࡴࡶࡥࡴ࠮ࠣࡸࡪࡹࡴࠡࡵࡦࡳࡵ࡫ࡳࠡࡹ࡬ࡰࡱࠦࡢࡦࠢࡵࡩࡸࡵ࡬ࡷࡧࡧࠤ࡮ࡴࠠࡄࡎࡌࠦᘢ"))
        return {
            TestFramework.bstack1lll11ll11l_opy_: uuid4().__str__(),
            TestFramework.bstack1ll11l1l1l1_opy_: test_id,
            TestFramework.bstack1l1lll1l1ll_opy_: test_name,
            TestFramework.bstack1ll1l1l11ll_opy_: getattr(test, bstack1lll11l_opy_ (u"ࠦࡳࡵࡤࡦ࡫ࡧࠦᘣ"), None),
            TestFramework.bstack1ll11ll1ll1_opy_: bstack1ll1l1ll11l_opy_,
            TestFramework.bstack1l1lll1lll1_opy_: bstack1l11lll1lll_opy_.__1ll1111lll1_opy_(test),
            TestFramework.bstack1ll11ll11l1_opy_: code,
            TestFramework.bstack1lll1lll11l_opy_: TestFramework.bstack1ll111111ll_opy_,
            TestFramework.bstack1lll1111lll_opy_: test_id,
            TestFramework.bstack1l111111ll1_opy_: bstack11lll1lllll_opy_
        }
    @staticmethod
    def __1ll1111lll1_opy_(test) -> List[str]:
        markers = []
        current = test
        while current:
            own_markers = getattr(current, bstack1lll11l_opy_ (u"ࠧࡵࡷ࡯ࡡࡰࡥࡷࡱࡥࡳࡵࠥᘤ"), [])
            markers.extend([getattr(m, bstack1lll11l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᘥ"), None) for m in own_markers if getattr(m, bstack1lll11l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᘦ"), None)])
            current = getattr(current, bstack1lll11l_opy_ (u"ࠣࡲࡤࡶࡪࡴࡴࠣᘧ"), None)
        return markers
    @staticmethod
    def __1ll11l1l111_opy_(location):
        return bstack1lll11l_opy_ (u"ࠤ࠽࠾ࠧᘨ").join(filter(lambda x: isinstance(x, str), location))