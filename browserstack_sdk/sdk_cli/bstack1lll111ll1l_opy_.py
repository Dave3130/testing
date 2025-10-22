# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
import json
import time
from datetime import datetime, timezone
from browserstack_sdk.sdk_cli.bstack1llll1ll111_opy_ import (
    bstack1lllllll1l1_opy_,
    bstack1llllll1l11_opy_,
    bstack1lll1111l1l_opy_,
    bstack1lllll111l1_opy_,
    bstack1lll1ll1l1l_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llll11l1ll_opy_ import bstack1llll1lllll_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1llll111l1l_opy_, bstack1lll1lll111_opy_, bstack1lll1l1llll_opy_
from browserstack_sdk.sdk_cli.bstack1lll11ll1ll_opy_ import bstack1lll1lll1l1_opy_
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1lll1ll11ll_opy_
from browserstack_sdk import sdk_pb2 as structs
from bstack_utils.measure import measure
from bstack_utils.constants import *
from typing import Tuple, List, Any
class bstack1lll11l11l1_opy_(bstack1lll1lll1l1_opy_):
    bstack1lll1l1lll1_opy_ = bstack1lllll1l_opy_ (u"ࠧࡺࡥࡴࡶࡢࡨࡷ࡯ࡶࡦࡴࡶࠦᅾ")
    bstack1lll1ll1ll1_opy_ = bstack1lllll1l_opy_ (u"ࠨࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡷࡪࡹࡳࡪࡱࡱࡷࠧᅿ")
    bstack1lll11llll1_opy_ = bstack1lllll1l_opy_ (u"ࠢ࡯ࡱࡱࡣࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡴࠤᆀ")
    bstack1lll1ll11l1_opy_ = bstack1lllll1l_opy_ (u"ࠣࡶࡨࡷࡹࡥࡳࡦࡵࡶ࡭ࡴࡴࡳࠣᆁ")
    bstack1llll111111_opy_ = bstack1lllll1l_opy_ (u"ࠤࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡩ࡯ࡵࡷࡥࡳࡩࡥࡠࡴࡨࡪࡸࠨᆂ")
    bstack1lll1l11lll_opy_ = bstack1lllll1l_opy_ (u"ࠥࡧࡧࡺ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠࡥࡵࡩࡦࡺࡥࡥࠤᆃ")
    bstack1lll11ll11l_opy_ = bstack1lllll1l_opy_ (u"ࠦࡨࡨࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡡࡱࡥࡲ࡫ࠢᆄ")
    bstack1llll11l111_opy_ = bstack1lllll1l_opy_ (u"ࠧࡩࡢࡵࡡࡶࡩࡸࡹࡩࡰࡰࡢࡷࡹࡧࡴࡶࡵࠥᆅ")
    def __init__(self):
        super().__init__(bstack1llll1111ll_opy_=self.bstack1lll1l1lll1_opy_, frameworks=[bstack1llll1lllll_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1llll1l1l11_opy_((bstack1llll111l1l_opy_.BEFORE_EACH, bstack1lll1lll111_opy_.POST), self.bstack1lll111lll1_opy_)
        TestFramework.bstack1llll1l1l11_opy_((bstack1llll111l1l_opy_.TEST, bstack1lll1lll111_opy_.PRE), self.bstack1lll1ll1111_opy_)
        TestFramework.bstack1llll1l1l11_opy_((bstack1llll111l1l_opy_.TEST, bstack1lll1lll111_opy_.POST), self.bstack1lll1l11l11_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll111lll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1llll_opy_,
        bstack1llll1l1lll_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1lll111_opy_],
        *args,
        **kwargs,
    ):
        bstack1lll1111l11_opy_ = self.bstack1lll111llll_opy_(instance.context)
        if not bstack1lll1111l11_opy_:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠨࡳࡦࡶࡢࡥࡨࡺࡩࡷࡧࡢࡨࡷ࡯ࡶࡦࡴࡶ࠾ࠥࡴ࡯ࠡࡦࡵ࡭ࡻ࡫ࡲࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࠤᆆ") + str(bstack1llll1l1lll_opy_) + bstack1lllll1l_opy_ (u"ࠢࠣᆇ"))
        f.bstack1llll11ll1l_opy_(instance, bstack1lll11l11l1_opy_.bstack1lll1ll1ll1_opy_, bstack1lll1111l11_opy_)
        bstack1lll111l1l1_opy_ = self.bstack1lll111llll_opy_(instance.context, bstack1lll1111ll1_opy_=False)
        f.bstack1llll11ll1l_opy_(instance, bstack1lll11l11l1_opy_.bstack1lll11llll1_opy_, bstack1lll111l1l1_opy_)
    def bstack1lll1ll1111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1llll_opy_,
        bstack1llll1l1lll_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1lll111_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll111lll1_opy_(f, instance, bstack1llll1l1lll_opy_, *args, **kwargs)
        if not f.get_state(instance, bstack1lll11l11l1_opy_.bstack1lll11ll11l_opy_, False):
            self.__1lll11l11ll_opy_(f,instance,bstack1llll1l1lll_opy_)
    def bstack1lll1l11l11_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1llll_opy_,
        bstack1llll1l1lll_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1lll111_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll111lll1_opy_(f, instance, bstack1llll1l1lll_opy_, *args, **kwargs)
        if not f.get_state(instance, bstack1lll11l11l1_opy_.bstack1lll11ll11l_opy_, False):
            self.__1lll11l11ll_opy_(f, instance, bstack1llll1l1lll_opy_)
        if not f.get_state(instance, bstack1lll11l11l1_opy_.bstack1llll11l111_opy_, False):
            self.__1lll11111l1_opy_(f, instance, bstack1llll1l1lll_opy_)
    def bstack1lll111l1ll_opy_(
        self,
        f: bstack1llll1lllll_opy_,
        driver: object,
        exec: Tuple[bstack1lllll111l1_opy_, str],
        bstack1llll1l1lll_opy_: Tuple[bstack1lllllll1l1_opy_, bstack1llllll1l11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if not f.bstack1lll1111lll_opy_(instance):
            return
        if f.get_state(instance, bstack1lll11l11l1_opy_.bstack1llll11l111_opy_, False):
            return
        driver.execute_script(
            bstack1lllll1l_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࢂࠨᆈ").format(
                json.dumps(
                    {
                        bstack1lllll1l_opy_ (u"ࠤࡤࡧࡹ࡯࡯࡯ࠤᆉ"): bstack1lllll1l_opy_ (u"ࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸࠨᆊ"),
                        bstack1lllll1l_opy_ (u"ࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢᆋ"): {bstack1lllll1l_opy_ (u"ࠧࡹࡴࡢࡶࡸࡷࠧᆌ"): result},
                    }
                )
            )
        )
        f.bstack1llll11ll1l_opy_(instance, bstack1lll11l11l1_opy_.bstack1llll11l111_opy_, True)
    def bstack1lll111llll_opy_(self, context: bstack1lll1ll1l1l_opy_, bstack1lll1111ll1_opy_= True):
        if bstack1lll1111ll1_opy_:
            bstack1lll1111l11_opy_ = self.bstack1llll1111l1_opy_(context, reverse=True)
        else:
            bstack1lll1111l11_opy_ = self.bstack1lll1ll111l_opy_(context, reverse=True)
        return [f for f in bstack1lll1111l11_opy_ if f[1].state != bstack1lllllll1l1_opy_.QUIT]
    @measure(event_name=EVENTS.bstack1l11lllll_opy_, stage=STAGE.bstack1l11ll1ll_opy_)
    def __1lll11111l1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1llll_opy_,
        bstack1llll1l1lll_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1lll111_opy_],
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack1lllll1l_opy_ (u"ࠨࡴࡦࡵࡷࡇࡴࡴࡴࡦࡺࡷࡓࡵࡺࡩࡰࡰࡶࠦᆍ")).get(bstack1lllll1l_opy_ (u"ࠢࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠦᆎ")):
            bstack1lll1111l11_opy_ = f.get_state(instance, bstack1lll11l11l1_opy_.bstack1lll1ll1ll1_opy_, [])
            if not bstack1lll1111l11_opy_:
                self.logger.debug(bstack1lllll1l_opy_ (u"ࠣࡵࡨࡸࡤࡧࡣࡵ࡫ࡹࡩࡤࡪࡲࡪࡸࡨࡶࡸࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࠦᆏ") + str(bstack1llll1l1lll_opy_) + bstack1lllll1l_opy_ (u"ࠤࠥᆐ"))
                return
            driver = bstack1lll1111l11_opy_[0][0]()
            status = f.get_state(instance, TestFramework.bstack1lll1l1111l_opy_, None)
            if not status:
                self.logger.debug(bstack1lllll1l_opy_ (u"ࠥࡷࡪࡺ࡟ࡢࡥࡷ࡭ࡻ࡫࡟ࡥࡴ࡬ࡺࡪࡸࡳ࠻ࠢࡱࡳࠥࡹࡴࡢࡶࡸࡷࠥ࡬࡯ࡳࠢࡷࡩࡸࡺࠬࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࠧᆑ") + str(bstack1llll1l1lll_opy_) + bstack1lllll1l_opy_ (u"ࠦࠧᆒ"))
                return
            bstack1lll11ll1l1_opy_ = {bstack1lllll1l_opy_ (u"ࠧࡹࡴࡢࡶࡸࡷࠧᆓ"): status.lower()}
            bstack1lll1llllll_opy_ = f.get_state(instance, TestFramework.bstack1lll11ll111_opy_, None)
            if status.lower() == bstack1lllll1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᆔ") and bstack1lll1llllll_opy_ is not None:
                bstack1lll11ll1l1_opy_[bstack1lllll1l_opy_ (u"ࠧࡳࡧࡤࡷࡴࡴࠧᆕ")] = bstack1lll1llllll_opy_[0][bstack1lllll1l_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫᆖ")][0] if isinstance(bstack1lll1llllll_opy_, list) else str(bstack1lll1llllll_opy_)
            driver.execute_script(
                bstack1lllll1l_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࢃࠢᆗ").format(
                    json.dumps(
                        {
                            bstack1lllll1l_opy_ (u"ࠥࡥࡨࡺࡩࡰࡰࠥᆘ"): bstack1lllll1l_opy_ (u"ࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠢᆙ"),
                            bstack1lllll1l_opy_ (u"ࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣᆚ"): bstack1lll11ll1l1_opy_,
                        }
                    )
                )
            )
            f.bstack1llll11ll1l_opy_(instance, bstack1lll11l11l1_opy_.bstack1llll11l111_opy_, True)
    @measure(event_name=EVENTS.bstack11l11l1ll_opy_, stage=STAGE.bstack1l11ll1ll_opy_)
    def __1lll11l11ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1llll_opy_,
        bstack1llll1l1lll_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1lll111_opy_]
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack1lllll1l_opy_ (u"ࠨࡴࡦࡵࡷࡇࡴࡴࡴࡦࡺࡷࡓࡵࡺࡩࡰࡰࡶࠦᆛ")).get(bstack1lllll1l_opy_ (u"ࠢࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤᆜ")):
            test_name = f.get_state(instance, TestFramework.bstack1lll111l11l_opy_, None)
            if not test_name:
                self.logger.debug(bstack1lllll1l_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡱ࡮ࡹࡳࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡱࡥࡲ࡫ࠢᆝ"))
                return
            bstack1lll1111l11_opy_ = f.get_state(instance, bstack1lll11l11l1_opy_.bstack1lll1ll1ll1_opy_, [])
            if not bstack1lll1111l11_opy_:
                self.logger.debug(bstack1lllll1l_opy_ (u"ࠤࡶࡩࡹࡥࡡࡤࡶ࡬ࡺࡪࡥࡤࡳ࡫ࡹࡩࡷࡹ࠺ࠡࡰࡲࠤࡸࡺࡡࡵࡷࡶࠤ࡫ࡵࡲࠡࡶࡨࡷࡹ࠲ࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࠦᆞ") + str(bstack1llll1l1lll_opy_) + bstack1lllll1l_opy_ (u"ࠥࠦᆟ"))
                return
            for bstack1lll111ll11_opy_, bstack1lll111111l_opy_ in bstack1lll1111l11_opy_:
                if not bstack1llll1lllll_opy_.bstack1lll1111lll_opy_(bstack1lll111111l_opy_):
                    continue
                driver = bstack1lll111ll11_opy_()
                if not driver:
                    continue
                driver.execute_script(
                    bstack1lllll1l_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠤᆠ").format(
                        json.dumps(
                            {
                                bstack1lllll1l_opy_ (u"ࠧࡧࡣࡵ࡫ࡲࡲࠧᆡ"): bstack1lllll1l_opy_ (u"ࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢᆢ"),
                                bstack1lllll1l_opy_ (u"ࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥᆣ"): {bstack1lllll1l_opy_ (u"ࠣࡰࡤࡱࡪࠨᆤ"): test_name},
                            }
                        )
                    )
                )
            f.bstack1llll11ll1l_opy_(instance, bstack1lll11l11l1_opy_.bstack1lll11ll11l_opy_, True)
    def bstack1lll1l11ll1_opy_(
        self,
        instance: bstack1lll1l1llll_opy_,
        f: TestFramework,
        bstack1llll1l1lll_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1lll111_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll111lll1_opy_(f, instance, bstack1llll1l1lll_opy_, *args, **kwargs)
        bstack1lll1111l11_opy_ = [d for d, _ in f.get_state(instance, bstack1lll11l11l1_opy_.bstack1lll1ll1ll1_opy_, [])]
        if not bstack1lll1111l11_opy_:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࠦࡳࡦࡵࡶ࡭ࡴࡴࡳࠡࡶࡲࠤࡱ࡯࡮࡬ࠤᆥ"))
            return
        if not bstack1lll1ll11ll_opy_():
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࡴࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠣᆦ"))
            return
        for bstack1lll11l111l_opy_ in bstack1lll1111l11_opy_:
            driver = bstack1lll11l111l_opy_()
            if not driver:
                continue
            timestamp = int(time.time() * 1000)
            data = bstack1lllll1l_opy_ (u"ࠦࡔࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࡗࡾࡴࡣ࠻ࠤᆧ") + str(timestamp)
            driver.execute_script(
                bstack1lllll1l_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠥᆨ").format(
                    json.dumps(
                        {
                            bstack1lllll1l_opy_ (u"ࠨࡡࡤࡶ࡬ࡳࡳࠨᆩ"): bstack1lllll1l_opy_ (u"ࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤᆪ"),
                            bstack1lllll1l_opy_ (u"ࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦᆫ"): {
                                bstack1lllll1l_opy_ (u"ࠤࡷࡽࡵ࡫ࠢᆬ"): bstack1lllll1l_opy_ (u"ࠥࡅࡳࡴ࡯ࡵࡣࡷ࡭ࡴࡴࠢᆭ"),
                                bstack1lllll1l_opy_ (u"ࠦࡩࡧࡴࡢࠤᆮ"): data,
                                bstack1lllll1l_opy_ (u"ࠧࡲࡥࡷࡧ࡯ࠦᆯ"): bstack1lllll1l_opy_ (u"ࠨࡤࡦࡤࡸ࡫ࠧᆰ")
                            }
                        }
                    )
                )
            )
    def bstack1lll1l11l1l_opy_(
        self,
        instance: bstack1lll1l1llll_opy_,
        f: TestFramework,
        bstack1llll1l1lll_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1lll111_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll111lll1_opy_(f, instance, bstack1llll1l1lll_opy_, *args, **kwargs)
        keys = [
            bstack1lll11l11l1_opy_.bstack1lll1ll1ll1_opy_,
            bstack1lll11l11l1_opy_.bstack1lll11llll1_opy_,
        ]
        bstack1lll1111l11_opy_ = []
        for key in keys:
            bstack1lll1111l11_opy_.extend(f.get_state(instance, key, []))
        if not bstack1lll1111l11_opy_:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡࡷࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡯࡮ࡥࠢࡤࡲࡾࠦࡳࡦࡵࡶ࡭ࡴࡴࡳࠡࡶࡲࠤࡱ࡯࡮࡬ࠤᆱ"))
            return
        if f.get_state(instance, bstack1lll11l11l1_opy_.bstack1lll1l11lll_opy_, False):
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠣࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡸࡪࡹࡴ࠻ࠢࡆࡆ࡙ࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡤࡴࡨࡥࡹ࡫ࡤࠣᆲ"))
            return
        self.bstack1llll1lll11_opy_()
        bstack1ll111ll1_opy_ = datetime.now()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1llllllllll_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1lll1l111l1_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll11lll11_opy_)
        req.test_framework_state = bstack1llll1l1lll_opy_[0].name
        req.test_hook_state = bstack1llll1l1lll_opy_[1].name
        req.test_uuid = TestFramework.get_state(instance, TestFramework.bstack1lll1lll1ll_opy_)
        for bstack1lll111ll11_opy_, driver in bstack1lll1111l11_opy_:
            try:
                webdriver = bstack1lll111ll11_opy_()
                if webdriver is None:
                    self.logger.debug(bstack1lllll1l_opy_ (u"ࠤ࡚ࡩࡧࡊࡲࡪࡸࡨࡶࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫ࠠࡪࡵࠣࡒࡴࡴࡥࠡࠪࡵࡩ࡫࡫ࡲࡦࡰࡦࡩࠥ࡫ࡸࡱ࡫ࡵࡩࡩ࠯ࠢᆳ"))
                    continue
                session = req.automation_sessions.add()
                session.provider = (
                    bstack1lllll1l_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠤᆴ")
                    if bstack1llll1lllll_opy_.get_state(driver, bstack1llll1lllll_opy_.bstack1lll111l111_opy_, False)
                    else bstack1lllll1l_opy_ (u"ࠦࡺࡴ࡫࡯ࡱࡺࡲࡤ࡭ࡲࡪࡦࠥᆵ")
                )
                session.ref = driver.ref()
                session.hub_url = bstack1llll1lllll_opy_.get_state(driver, bstack1llll1lllll_opy_.bstack1lll1lllll1_opy_, bstack1lllll1l_opy_ (u"ࠧࠨᆶ"))
                session.framework_name = driver.framework_name
                session.framework_version = driver.framework_version
                session.framework_session_id = bstack1llll1lllll_opy_.get_state(driver, bstack1llll1lllll_opy_.bstack1lll1llll1l_opy_, bstack1lllll1l_opy_ (u"ࠨࠢᆷ"))
                caps = None
                if hasattr(webdriver, bstack1lllll1l_opy_ (u"ࠢࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠨᆸ")):
                    try:
                        caps = webdriver.capabilities
                        self.logger.debug(bstack1lllll1l_opy_ (u"ࠣࡕࡸࡧࡨ࡫ࡳࡴࡨࡸࡰࡱࡿࠠࡳࡧࡷࡶ࡮࡫ࡶࡦࡦࠣࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠢࡧ࡭ࡷ࡫ࡣࡵ࡮ࡼࠤ࡫ࡸ࡯࡮ࠢࡧࡶ࡮ࡼࡥࡳ࠰ࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣᆹ"))
                    except Exception as e:
                        self.logger.debug(bstack1lllll1l_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥ࡭ࡥࡵࠢࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠡࡨࡵࡳࡲࠦࡤࡳ࡫ࡹࡩࡷ࠴ࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷ࠿ࠦࠢᆺ") + str(e) + bstack1lllll1l_opy_ (u"ࠥࠦᆻ"))
                try:
                    bstack1lll11111ll_opy_ = json.dumps(caps).encode(bstack1lllll1l_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥᆼ")) if caps else bstack1lll11l1111_opy_ (u"ࠧࢁࡽࠣᆽ")
                    req.capabilities = bstack1lll11111ll_opy_
                except Exception as e:
                    self.logger.debug(bstack1lllll1l_opy_ (u"ࠨࡧࡦࡶࡢࡧࡧࡺ࡟ࡦࡸࡨࡲࡹࡀࠠࡧࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡴࡤࠡࡵࡨࡶ࡮ࡧ࡬ࡪࡼࡨࠤࡨࡧࡰࡴࠢࡩࡳࡷࠦࡲࡦࡳࡸࡩࡸࡺ࠺ࠡࠤᆾ") + str(e) + bstack1lllll1l_opy_ (u"ࠢࠣᆿ"))
            except Exception as e:
                self.logger.error(bstack1lllll1l_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡱࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤࡩࡸࡩࡷࡧࡵࠤ࡮ࡺࡥ࡮࠼ࠣࠦᇀ") + str(str(e)) + bstack1lllll1l_opy_ (u"ࠤࠥᇁ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1lll1l111ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1llll_opy_,
        bstack1llll1l1lll_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1lll111_opy_],
        *args,
        **kwargs
    ):
        bstack1lll1111l11_opy_ = f.get_state(instance, bstack1lll11l11l1_opy_.bstack1lll1ll1ll1_opy_, [])
        if not bstack1lll1ll11ll_opy_() and len(bstack1lll1111l11_opy_) == 0:
            bstack1lll1111l11_opy_ = f.get_state(instance, bstack1lll11l11l1_opy_.bstack1lll11llll1_opy_, [])
        if not bstack1lll1111l11_opy_:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᇂ") + str(kwargs) + bstack1lllll1l_opy_ (u"ࠦࠧᇃ"))
            return {}
        if len(bstack1lll1111l11_opy_) > 1:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠࡼ࡮ࡨࡲ࠭ࡪࡲࡪࡸࡨࡶࡤ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳࠪࡿࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᇄ") + str(kwargs) + bstack1lllll1l_opy_ (u"ࠨࠢᇅ"))
            return {}
        bstack1lll111ll11_opy_, bstack1lll1l1l11l_opy_ = bstack1lll1111l11_opy_[0]
        driver = bstack1lll111ll11_opy_()
        if not driver:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᇆ") + str(kwargs) + bstack1lllll1l_opy_ (u"ࠣࠤᇇ"))
            return {}
        capabilities = f.get_state(bstack1lll1l1l11l_opy_, bstack1llll1lllll_opy_.bstack1llll111l11_opy_)
        if not capabilities:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠦࡦࡰࡷࡱࡨࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᇈ") + str(kwargs) + bstack1lllll1l_opy_ (u"ࠥࠦᇉ"))
            return {}
        return capabilities.get(bstack1lllll1l_opy_ (u"ࠦࡦࡲࡷࡢࡻࡶࡑࡦࡺࡣࡩࠤᇊ"), {})
    def bstack1lll1l1l111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1llll_opy_,
        bstack1llll1l1lll_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1lll111_opy_],
        *args,
        **kwargs
    ):
        bstack1lll1111l11_opy_ = f.get_state(instance, bstack1lll11l11l1_opy_.bstack1lll1ll1ll1_opy_, [])
        if not bstack1lll1ll11ll_opy_() and len(bstack1lll1111l11_opy_) == 0:
            bstack1lll1111l11_opy_ = f.get_state(instance, bstack1lll11l11l1_opy_.bstack1lll11llll1_opy_, [])
        if not bstack1lll1111l11_opy_:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠧ࡭ࡥࡵࡡࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡤࡳ࡫ࡹࡩࡷࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᇋ") + str(kwargs) + bstack1lllll1l_opy_ (u"ࠨࠢᇌ"))
            return
        if len(bstack1lll1111l11_opy_) > 1:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠢࡨࡧࡷࡣࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡦࡵ࡭ࡻ࡫ࡲ࠻ࠢࡾࡰࡪࡴࠨࡥࡴ࡬ࡺࡪࡸ࡟ࡪࡰࡶࡸࡦࡴࡣࡦࡵࠬࢁࠥࡪࡲࡪࡸࡨࡶࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᇍ") + str(kwargs) + bstack1lllll1l_opy_ (u"ࠣࠤᇎ"))
        bstack1lll111ll11_opy_, bstack1lll1l1l11l_opy_ = bstack1lll1111l11_opy_[0]
        driver = bstack1lll111ll11_opy_()
        if not driver:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠤࡪࡩࡹࡥࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡨࡷ࡯ࡶࡦࡴ࠽ࠤࡳࡵࠠࡥࡴ࡬ࡺࡪࡸࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᇏ") + str(kwargs) + bstack1lllll1l_opy_ (u"ࠥࠦᇐ"))
            return
        return driver