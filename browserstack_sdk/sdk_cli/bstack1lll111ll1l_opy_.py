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
import json
import time
from datetime import datetime, timezone
from browserstack_sdk.sdk_cli.bstack1lllll1l1ll_opy_ import (
    bstack1llll1l1l1l_opy_,
    bstack1lllllll111_opy_,
    bstack1lll111ll11_opy_,
    bstack1llll11l1ll_opy_,
    bstack1lll1l1111l_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llll1l11ll_opy_ import bstack1lllllll11l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l1llll_opy_, bstack1lll11lll1l_opy_, bstack1lll1l1ll11_opy_
from browserstack_sdk.sdk_cli.bstack1llll111111_opy_ import bstack1lll1l1lll1_opy_
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1lll1ll1lll_opy_
from browserstack_sdk import sdk_pb2 as structs
from bstack_utils.measure import measure
from bstack_utils.constants import *
from typing import Tuple, List, Any
class bstack1lll111lll1_opy_(bstack1lll1l1lll1_opy_):
    bstack1llll111l1l_opy_ = bstack11l1l11_opy_ (u"ࠣࡶࡨࡷࡹࡥࡤࡳ࡫ࡹࡩࡷࡹࠢᅺ")
    bstack1lll1ll1l1l_opy_ = bstack11l1l11_opy_ (u"ࠤࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡳࡦࡵࡶ࡭ࡴࡴࡳࠣᅻ")
    bstack1lll1l11ll1_opy_ = bstack11l1l11_opy_ (u"ࠥࡲࡴࡴ࡟ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡷࡪࡹࡳࡪࡱࡱࡷࠧᅼ")
    bstack1lll11ll1l1_opy_ = bstack11l1l11_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡶࡩࡸࡹࡩࡰࡰࡶࠦᅽ")
    bstack1lll1ll1ll1_opy_ = bstack11l1l11_opy_ (u"ࠧࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡣࡷ࡫ࡦࡴࠤᅾ")
    bstack1lll1lll11l_opy_ = bstack11l1l11_opy_ (u"ࠨࡣࡣࡶࡢࡷࡪࡹࡳࡪࡱࡱࡣࡨࡸࡥࡢࡶࡨࡨࠧᅿ")
    bstack1lll1l111ll_opy_ = bstack11l1l11_opy_ (u"ࠢࡤࡤࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡴࡡ࡮ࡧࠥᆀ")
    bstack1lll1ll11ll_opy_ = bstack11l1l11_opy_ (u"ࠣࡥࡥࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡳࡵࡣࡷࡹࡸࠨᆁ")
    def __init__(self):
        super().__init__(bstack1lll1l1l1l1_opy_=self.bstack1llll111l1l_opy_, frameworks=[bstack1lllllll11l_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1llll1ll1ll_opy_((bstack1lll1l1llll_opy_.BEFORE_EACH, bstack1lll11lll1l_opy_.POST), self.bstack1lll1111l11_opy_)
        TestFramework.bstack1llll1ll1ll_opy_((bstack1lll1l1llll_opy_.TEST, bstack1lll11lll1l_opy_.PRE), self.bstack1lll11l1ll1_opy_)
        TestFramework.bstack1llll1ll1ll_opy_((bstack1lll1l1llll_opy_.TEST, bstack1lll11lll1l_opy_.POST), self.bstack1llll111lll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll1111l11_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll11_opy_,
        bstack1llllll11l1_opy_: Tuple[bstack1lll1l1llll_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs,
    ):
        bstack1lll111l11l_opy_ = self.bstack1lll1111l1l_opy_(instance.context)
        if not bstack1lll111l11l_opy_:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠤࡶࡩࡹࡥࡡࡤࡶ࡬ࡺࡪࡥࡤࡳ࡫ࡹࡩࡷࡹ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࠧᆂ") + str(bstack1llllll11l1_opy_) + bstack11l1l11_opy_ (u"ࠥࠦᆃ"))
        f.bstack1llllll1l11_opy_(instance, bstack1lll111lll1_opy_.bstack1lll1ll1l1l_opy_, bstack1lll111l11l_opy_)
        bstack1lll1111111_opy_ = self.bstack1lll1111l1l_opy_(instance.context, bstack1lll111111l_opy_=False)
        f.bstack1llllll1l11_opy_(instance, bstack1lll111lll1_opy_.bstack1lll1l11ll1_opy_, bstack1lll1111111_opy_)
    def bstack1lll11l1ll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll11_opy_,
        bstack1llllll11l1_opy_: Tuple[bstack1lll1l1llll_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1111l11_opy_(f, instance, bstack1llllll11l1_opy_, *args, **kwargs)
        if not f.get_state(instance, bstack1lll111lll1_opy_.bstack1lll1l111ll_opy_, False):
            self.__1lll1111ll1_opy_(f,instance,bstack1llllll11l1_opy_)
    def bstack1llll111lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll11_opy_,
        bstack1llllll11l1_opy_: Tuple[bstack1lll1l1llll_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1111l11_opy_(f, instance, bstack1llllll11l1_opy_, *args, **kwargs)
        if not f.get_state(instance, bstack1lll111lll1_opy_.bstack1lll1l111ll_opy_, False):
            self.__1lll1111ll1_opy_(f, instance, bstack1llllll11l1_opy_)
        if not f.get_state(instance, bstack1lll111lll1_opy_.bstack1lll1ll11ll_opy_, False):
            self.__1lll11111ll_opy_(f, instance, bstack1llllll11l1_opy_)
    def bstack1ll1lllllll_opy_(
        self,
        f: bstack1lllllll11l_opy_,
        driver: object,
        exec: Tuple[bstack1llll11l1ll_opy_, str],
        bstack1llllll11l1_opy_: Tuple[bstack1llll1l1l1l_opy_, bstack1lllllll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if not f.bstack1lll11l1111_opy_(instance):
            return
        if f.get_state(instance, bstack1lll111lll1_opy_.bstack1lll1ll11ll_opy_, False):
            return
        driver.execute_script(
            bstack11l1l11_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠤᆄ").format(
                json.dumps(
                    {
                        bstack11l1l11_opy_ (u"ࠧࡧࡣࡵ࡫ࡲࡲࠧᆅ"): bstack11l1l11_opy_ (u"ࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠤᆆ"),
                        bstack11l1l11_opy_ (u"ࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥᆇ"): {bstack11l1l11_opy_ (u"ࠣࡵࡷࡥࡹࡻࡳࠣᆈ"): result},
                    }
                )
            )
        )
        f.bstack1llllll1l11_opy_(instance, bstack1lll111lll1_opy_.bstack1lll1ll11ll_opy_, True)
    def bstack1lll1111l1l_opy_(self, context: bstack1lll1l1111l_opy_, bstack1lll111111l_opy_= True):
        if bstack1lll111111l_opy_:
            bstack1lll111l11l_opy_ = self.bstack1lll11lll11_opy_(context, reverse=True)
        else:
            bstack1lll111l11l_opy_ = self.bstack1lll11llll1_opy_(context, reverse=True)
        return [f for f in bstack1lll111l11l_opy_ if f[1].state != bstack1llll1l1l1l_opy_.QUIT]
    @measure(event_name=EVENTS.bstack1111l1ll1l_opy_, stage=STAGE.bstack111llllll_opy_)
    def __1lll11111ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll11_opy_,
        bstack1llllll11l1_opy_: Tuple[bstack1lll1l1llll_opy_, bstack1lll11lll1l_opy_],
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack11l1l11_opy_ (u"ࠤࡷࡩࡸࡺࡃࡰࡰࡷࡩࡽࡺࡏࡱࡶ࡬ࡳࡳࡹࠢᆉ")).get(bstack11l1l11_opy_ (u"ࠥࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠢᆊ")):
            bstack1lll111l11l_opy_ = f.get_state(instance, bstack1lll111lll1_opy_.bstack1lll1ll1l1l_opy_, [])
            if not bstack1lll111l11l_opy_:
                self.logger.debug(bstack11l1l11_opy_ (u"ࠦࡸ࡫ࡴࡠࡣࡦࡸ࡮ࡼࡥࡠࡦࡵ࡭ࡻ࡫ࡲࡴ࠼ࠣࡲࡴࠦࡤࡳ࡫ࡹࡩࡷࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࠢᆋ") + str(bstack1llllll11l1_opy_) + bstack11l1l11_opy_ (u"ࠧࠨᆌ"))
                return
            driver = bstack1lll111l11l_opy_[0][0]()
            status = f.get_state(instance, TestFramework.bstack1lll11l1l1l_opy_, None)
            if not status:
                self.logger.debug(bstack11l1l11_opy_ (u"ࠨࡳࡦࡶࡢࡥࡨࡺࡩࡷࡧࡢࡨࡷ࡯ࡶࡦࡴࡶ࠾ࠥࡴ࡯ࠡࡵࡷࡥࡹࡻࡳࠡࡨࡲࡶࠥࡺࡥࡴࡶ࠯ࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࠣᆍ") + str(bstack1llllll11l1_opy_) + bstack11l1l11_opy_ (u"ࠢࠣᆎ"))
                return
            bstack1llll111l11_opy_ = {bstack11l1l11_opy_ (u"ࠣࡵࡷࡥࡹࡻࡳࠣᆏ"): status.lower()}
            bstack1llll11111l_opy_ = f.get_state(instance, TestFramework.bstack1lll1llll11_opy_, None)
            if status.lower() == bstack11l1l11_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᆐ") and bstack1llll11111l_opy_ is not None:
                bstack1llll111l11_opy_[bstack11l1l11_opy_ (u"ࠪࡶࡪࡧࡳࡰࡰࠪᆑ")] = bstack1llll11111l_opy_[0][bstack11l1l11_opy_ (u"ࠫࡧࡧࡣ࡬ࡶࡵࡥࡨ࡫ࠧᆒ")][0] if isinstance(bstack1llll11111l_opy_, list) else str(bstack1llll11111l_opy_)
            driver.execute_script(
                bstack11l1l11_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠥᆓ").format(
                    json.dumps(
                        {
                            bstack11l1l11_opy_ (u"ࠨࡡࡤࡶ࡬ࡳࡳࠨᆔ"): bstack11l1l11_opy_ (u"ࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠥᆕ"),
                            bstack11l1l11_opy_ (u"ࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦᆖ"): bstack1llll111l11_opy_,
                        }
                    )
                )
            )
            f.bstack1llllll1l11_opy_(instance, bstack1lll111lll1_opy_.bstack1lll1ll11ll_opy_, True)
    @measure(event_name=EVENTS.bstack111l1ll11l_opy_, stage=STAGE.bstack111llllll_opy_)
    def __1lll1111ll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll11_opy_,
        bstack1llllll11l1_opy_: Tuple[bstack1lll1l1llll_opy_, bstack1lll11lll1l_opy_]
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack11l1l11_opy_ (u"ࠤࡷࡩࡸࡺࡃࡰࡰࡷࡩࡽࡺࡏࡱࡶ࡬ࡳࡳࡹࠢᆗ")).get(bstack11l1l11_opy_ (u"ࠥࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧᆘ")):
            test_name = f.get_state(instance, TestFramework.bstack1lll111l111_opy_, None)
            if not test_name:
                self.logger.debug(bstack11l1l11_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡭ࡪࡵࡶ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡴࡡ࡮ࡧࠥᆙ"))
                return
            bstack1lll111l11l_opy_ = f.get_state(instance, bstack1lll111lll1_opy_.bstack1lll1ll1l1l_opy_, [])
            if not bstack1lll111l11l_opy_:
                self.logger.debug(bstack11l1l11_opy_ (u"ࠧࡹࡥࡵࡡࡤࡧࡹ࡯ࡶࡦࡡࡧࡶ࡮ࡼࡥࡳࡵ࠽ࠤࡳࡵࠠࡴࡶࡤࡸࡺࡹࠠࡧࡱࡵࠤࡹ࡫ࡳࡵ࠮ࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࠢᆚ") + str(bstack1llllll11l1_opy_) + bstack11l1l11_opy_ (u"ࠨࠢᆛ"))
                return
            for bstack1lll111llll_opy_, bstack1lll11111l1_opy_ in bstack1lll111l11l_opy_:
                if not bstack1lllllll11l_opy_.bstack1lll11l1111_opy_(bstack1lll11111l1_opy_):
                    continue
                driver = bstack1lll111llll_opy_()
                if not driver:
                    continue
                driver.execute_script(
                    bstack11l1l11_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠧᆜ").format(
                        json.dumps(
                            {
                                bstack11l1l11_opy_ (u"ࠣࡣࡦࡸ࡮ࡵ࡮ࠣᆝ"): bstack11l1l11_opy_ (u"ࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥᆞ"),
                                bstack11l1l11_opy_ (u"ࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨᆟ"): {bstack11l1l11_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᆠ"): test_name},
                            }
                        )
                    )
                )
            f.bstack1llllll1l11_opy_(instance, bstack1lll111lll1_opy_.bstack1lll1l111ll_opy_, True)
    def bstack1lll1l1ll1l_opy_(
        self,
        instance: bstack1lll1l1ll11_opy_,
        f: TestFramework,
        bstack1llllll11l1_opy_: Tuple[bstack1lll1l1llll_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1111l11_opy_(f, instance, bstack1llllll11l1_opy_, *args, **kwargs)
        bstack1lll111l11l_opy_ = [d for d, _ in f.get_state(instance, bstack1lll111lll1_opy_.bstack1lll1ll1l1l_opy_, [])]
        if not bstack1lll111l11l_opy_:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡶࡩࡸࡹࡩࡰࡰࡶࠤࡹࡵࠠ࡭࡫ࡱ࡯ࠧᆡ"))
            return
        if not bstack1lll1ll1lll_opy_():
            self.logger.debug(bstack11l1l11_opy_ (u"ࠨ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࡷࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠦᆢ"))
            return
        for bstack1lll1111lll_opy_ in bstack1lll111l11l_opy_:
            driver = bstack1lll1111lll_opy_()
            if not driver:
                continue
            timestamp = int(time.time() * 1000)
            data = bstack11l1l11_opy_ (u"ࠢࡐࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࡓࡺࡰࡦ࠾ࠧᆣ") + str(timestamp)
            driver.execute_script(
                bstack11l1l11_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࢂࠨᆤ").format(
                    json.dumps(
                        {
                            bstack11l1l11_opy_ (u"ࠤࡤࡧࡹ࡯࡯࡯ࠤᆥ"): bstack11l1l11_opy_ (u"ࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧᆦ"),
                            bstack11l1l11_opy_ (u"ࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢᆧ"): {
                                bstack11l1l11_opy_ (u"ࠧࡺࡹࡱࡧࠥᆨ"): bstack11l1l11_opy_ (u"ࠨࡁ࡯ࡰࡲࡸࡦࡺࡩࡰࡰࠥᆩ"),
                                bstack11l1l11_opy_ (u"ࠢࡥࡣࡷࡥࠧᆪ"): data,
                                bstack11l1l11_opy_ (u"ࠣ࡮ࡨࡺࡪࡲࠢᆫ"): bstack11l1l11_opy_ (u"ࠤࡧࡩࡧࡻࡧࠣᆬ")
                            }
                        }
                    )
                )
            )
    def bstack1lll1ll111l_opy_(
        self,
        instance: bstack1lll1l1ll11_opy_,
        f: TestFramework,
        bstack1llllll11l1_opy_: Tuple[bstack1lll1l1llll_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1111l11_opy_(f, instance, bstack1llllll11l1_opy_, *args, **kwargs)
        keys = [
            bstack1lll111lll1_opy_.bstack1lll1ll1l1l_opy_,
            bstack1lll111lll1_opy_.bstack1lll1l11ll1_opy_,
        ]
        bstack1lll111l11l_opy_ = []
        for key in keys:
            bstack1lll111l11l_opy_.extend(f.get_state(instance, key, []))
        if not bstack1lll111l11l_opy_:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࡺࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡧ࡫ࡱࡨࠥࡧ࡮ࡺࠢࡶࡩࡸࡹࡩࡰࡰࡶࠤࡹࡵࠠ࡭࡫ࡱ࡯ࠧᆭ"))
            return
        if f.get_state(instance, bstack1lll111lll1_opy_.bstack1lll1lll11l_opy_, False):
            self.logger.debug(bstack11l1l11_opy_ (u"ࠦࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡴࡦࡵࡷ࠾ࠥࡉࡂࡕࠢࡤࡰࡷ࡫ࡡࡥࡻࠣࡧࡷ࡫ࡡࡵࡧࡧࠦᆮ"))
            return
        self.bstack1lllll1l111_opy_()
        bstack1ll1111ll_opy_ = datetime.now()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1llll1lll11_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1lll1lll1l1_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll11lllll_opy_)
        req.test_framework_state = bstack1llllll11l1_opy_[0].name
        req.test_hook_state = bstack1llllll11l1_opy_[1].name
        req.test_uuid = TestFramework.get_state(instance, TestFramework.bstack1llll111ll1_opy_)
        for bstack1lll111llll_opy_, driver in bstack1lll111l11l_opy_:
            try:
                webdriver = bstack1lll111llll_opy_()
                if webdriver is None:
                    self.logger.debug(bstack11l1l11_opy_ (u"ࠧ࡝ࡥࡣࡆࡵ࡭ࡻ࡫ࡲࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࠣ࡭ࡸࠦࡎࡰࡰࡨࠤ࠭ࡸࡥࡧࡧࡵࡩࡳࡩࡥࠡࡧࡻࡴ࡮ࡸࡥࡥࠫࠥᆯ"))
                    continue
                session = req.automation_sessions.add()
                session.provider = (
                    bstack11l1l11_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠧᆰ")
                    if bstack1lllllll11l_opy_.get_state(driver, bstack1lllllll11l_opy_.bstack1lll111l1l1_opy_, False)
                    else bstack11l1l11_opy_ (u"ࠢࡶࡰ࡮ࡲࡴࡽ࡮ࡠࡩࡵ࡭ࡩࠨᆱ")
                )
                session.ref = driver.ref()
                session.hub_url = bstack1lllllll11l_opy_.get_state(driver, bstack1lllllll11l_opy_.bstack1lll11l1lll_opy_, bstack11l1l11_opy_ (u"ࠣࠤᆲ"))
                session.framework_name = driver.framework_name
                session.framework_version = driver.framework_version
                session.framework_session_id = bstack1lllllll11l_opy_.get_state(driver, bstack1lllllll11l_opy_.bstack1lll1l1l111_opy_, bstack11l1l11_opy_ (u"ࠤࠥᆳ"))
                caps = None
                if hasattr(webdriver, bstack11l1l11_opy_ (u"ࠥࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠤᆴ")):
                    try:
                        caps = webdriver.capabilities
                        self.logger.debug(bstack11l1l11_opy_ (u"ࠦࡘࡻࡣࡤࡧࡶࡷ࡫ࡻ࡬࡭ࡻࠣࡶࡪࡺࡲࡪࡧࡹࡩࡩࠦࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠥࡪࡩࡳࡧࡦࡸࡱࡿࠠࡧࡴࡲࡱࠥࡪࡲࡪࡸࡨࡶ࠳ࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠦᆵ"))
                    except Exception as e:
                        self.logger.debug(bstack11l1l11_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡩࡨࡸࠥࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠤ࡫ࡸ࡯࡮ࠢࡧࡶ࡮ࡼࡥࡳ࠰ࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳ࠻ࠢࠥᆶ") + str(e) + bstack11l1l11_opy_ (u"ࠨࠢᆷ"))
                try:
                    bstack1lll11l111l_opy_ = json.dumps(caps).encode(bstack11l1l11_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨᆸ")) if caps else bstack1lll111l1ll_opy_ (u"ࠣࡽࢀࠦᆹ")
                    req.capabilities = bstack1lll11l111l_opy_
                except Exception as e:
                    self.logger.debug(bstack11l1l11_opy_ (u"ࠤࡪࡩࡹࡥࡣࡣࡶࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡪࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡰࡧࠤࡸ࡫ࡲࡪࡣ࡯࡭ࡿ࡫ࠠࡤࡣࡳࡷࠥ࡬࡯ࡳࠢࡵࡩࡶࡻࡥࡴࡶ࠽ࠤࠧᆺ") + str(e) + bstack11l1l11_opy_ (u"ࠥࠦᆻ"))
            except Exception as e:
                self.logger.error(bstack11l1l11_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡴࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡥࡴ࡬ࡺࡪࡸࠠࡪࡶࡨࡱ࠿ࠦࠢᆼ") + str(str(e)) + bstack11l1l11_opy_ (u"ࠧࠨᆽ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1lll1l11l1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll11_opy_,
        bstack1llllll11l1_opy_: Tuple[bstack1lll1l1llll_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs
    ):
        bstack1lll111l11l_opy_ = f.get_state(instance, bstack1lll111lll1_opy_.bstack1lll1ll1l1l_opy_, [])
        if not bstack1lll1ll1lll_opy_() and len(bstack1lll111l11l_opy_) == 0:
            bstack1lll111l11l_opy_ = f.get_state(instance, bstack1lll111lll1_opy_.bstack1lll1l11ll1_opy_, [])
        if not bstack1lll111l11l_opy_:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᆾ") + str(kwargs) + bstack11l1l11_opy_ (u"ࠢࠣᆿ"))
            return {}
        if len(bstack1lll111l11l_opy_) > 1:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡿࡱ࡫࡮ࠩࡦࡵ࡭ࡻ࡫ࡲࡠ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡶ࠭ࢂࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᇀ") + str(kwargs) + bstack11l1l11_opy_ (u"ࠤࠥᇁ"))
            return {}
        bstack1lll111llll_opy_, bstack1lll11ll1ll_opy_ = bstack1lll111l11l_opy_[0]
        driver = bstack1lll111llll_opy_()
        if not driver:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࠡࡦࡵ࡭ࡻ࡫ࡲࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᇂ") + str(kwargs) + bstack11l1l11_opy_ (u"ࠦࠧᇃ"))
            return {}
        capabilities = f.get_state(bstack1lll11ll1ll_opy_, bstack1lllllll11l_opy_.bstack1lll1lllll1_opy_)
        if not capabilities:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠢࡩࡳࡺࡴࡤࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᇄ") + str(kwargs) + bstack11l1l11_opy_ (u"ࠨࠢᇅ"))
            return {}
        return capabilities.get(bstack11l1l11_opy_ (u"ࠢࡢ࡮ࡺࡥࡾࡹࡍࡢࡶࡦ࡬ࠧᇆ"), {})
    def bstack1lll1ll1111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll11_opy_,
        bstack1llllll11l1_opy_: Tuple[bstack1lll1l1llll_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs
    ):
        bstack1lll111l11l_opy_ = f.get_state(instance, bstack1lll111lll1_opy_.bstack1lll1ll1l1l_opy_, [])
        if not bstack1lll1ll1lll_opy_() and len(bstack1lll111l11l_opy_) == 0:
            bstack1lll111l11l_opy_ = f.get_state(instance, bstack1lll111lll1_opy_.bstack1lll1l11ll1_opy_, [])
        if not bstack1lll111l11l_opy_:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠣࡩࡨࡸࡤࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡧࡶ࡮ࡼࡥࡳ࠼ࠣࡲࡴࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᇇ") + str(kwargs) + bstack11l1l11_opy_ (u"ࠤࠥᇈ"))
            return
        if len(bstack1lll111l11l_opy_) > 1:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡩࡸࡩࡷࡧࡵ࠾ࠥࢁ࡬ࡦࡰࠫࡨࡷ࡯ࡶࡦࡴࡢ࡭ࡳࡹࡴࡢࡰࡦࡩࡸ࠯ࡽࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᇉ") + str(kwargs) + bstack11l1l11_opy_ (u"ࠦࠧᇊ"))
        bstack1lll111llll_opy_, bstack1lll11ll1ll_opy_ = bstack1lll111l11l_opy_[0]
        driver = bstack1lll111llll_opy_()
        if not driver:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠧ࡭ࡥࡵࡡࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡤࡳ࡫ࡹࡩࡷࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᇋ") + str(kwargs) + bstack11l1l11_opy_ (u"ࠨࠢᇌ"))
            return
        return driver