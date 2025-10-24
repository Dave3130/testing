# coding: UTF-8
import sys
bstack1lll1_opy_ = sys.version_info [0] == 2
bstack11l11_opy_ = 2048
bstack1_opy_ = 7
def bstack1l1_opy_ (bstack1llllll_opy_):
    global bstack1l11111_opy_
    bstack1l111l_opy_ = ord (bstack1llllll_opy_ [-1])
    bstack11l1ll1_opy_ = bstack1llllll_opy_ [:-1]
    bstack11l1l1l_opy_ = bstack1l111l_opy_ % len (bstack11l1ll1_opy_)
    bstack11111l1_opy_ = bstack11l1ll1_opy_ [:bstack11l1l1l_opy_] + bstack11l1ll1_opy_ [bstack11l1l1l_opy_:]
    if bstack1lll1_opy_:
        bstack1lllll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    else:
        bstack1lllll1_opy_ = str () .join ([chr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    return eval (bstack1lllll1_opy_)
import json
import time
import os
import threading
import asyncio
from browserstack_sdk.sdk_cli.bstack1llll11ll1l_opy_ import (
    bstack1llllll111l_opy_,
    bstack1llll1l111l_opy_,
    bstack1llllll1l1l_opy_,
    bstack1llll111111_opy_,
)
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1lll1ll111l_opy_, bstack1l11l11ll_opy_
from browserstack_sdk.sdk_cli.bstack1111111l11_opy_ import bstack1llll1l11l1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1llll11l11l_opy_, bstack1lll11llll1_opy_, bstack1lll1l11111_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l1ll11_opy_ import bstack1llll111l11_opy_
from browserstack_sdk.sdk_cli.bstack1llll11l1l1_opy_ import bstack1lll11lll1l_opy_
from typing import Tuple, List, Any
from bstack_utils.bstack1l11l1llll_opy_ import bstack1111l1111_opy_, bstack1l1ll11l11_opy_, bstack1ll1ll1l11_opy_
from browserstack_sdk import sdk_pb2 as structs
class bstack1lll1ll1l1l_opy_(bstack1lll11lll1l_opy_):
    bstack1lll1l1llll_opy_ = bstack1l1_opy_ (u"ࠢࡵࡧࡶࡸࡤࡪࡲࡪࡸࡨࡶࡸࠨᄗ")
    bstack1llll1111l1_opy_ = bstack1l1_opy_ (u"ࠣࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡹࡥࡴࡵ࡬ࡳࡳࡹࠢᄘ")
    bstack1lll1ll1111_opy_ = bstack1l1_opy_ (u"ࠤࡱࡳࡳࡥࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡶࡩࡸࡹࡩࡰࡰࡶࠦᄙ")
    bstack1llll1111ll_opy_ = bstack1l1_opy_ (u"ࠥࡸࡪࡹࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡵࠥᄚ")
    bstack1lll1lll111_opy_ = bstack1l1_opy_ (u"ࠦࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡢࡶࡪ࡬ࡳࠣᄛ")
    bstack1lll1l111ll_opy_ = bstack1l1_opy_ (u"ࠧࡩࡢࡵࡡࡶࡩࡸࡹࡩࡰࡰࡢࡧࡷ࡫ࡡࡵࡧࡧࠦᄜ")
    bstack1lll1l11ll1_opy_ = bstack1l1_opy_ (u"ࠨࡣࡣࡶࡢࡷࡪࡹࡳࡪࡱࡱࡣࡳࡧ࡭ࡦࠤᄝ")
    bstack1lll1l111l1_opy_ = bstack1l1_opy_ (u"ࠢࡤࡤࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡹࡴࡢࡶࡸࡷࠧᄞ")
    def __init__(self):
        super().__init__(bstack1lll11lllll_opy_=self.bstack1lll1l1llll_opy_, frameworks=[bstack1llll1l11l1_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1llll1ll1l1_opy_((bstack1llll11l11l_opy_.BEFORE_EACH, bstack1lll11llll1_opy_.POST), self.bstack1llll111lll_opy_)
        if bstack1l11l11ll_opy_():
            TestFramework.bstack1llll1ll1l1_opy_((bstack1llll11l11l_opy_.TEST, bstack1lll11llll1_opy_.POST), self.bstack1lll1l11lll_opy_)
        else:
            TestFramework.bstack1llll1ll1l1_opy_((bstack1llll11l11l_opy_.TEST, bstack1lll11llll1_opy_.PRE), self.bstack1lll1l11lll_opy_)
        TestFramework.bstack1llll1ll1l1_opy_((bstack1llll11l11l_opy_.TEST, bstack1lll11llll1_opy_.POST), self.bstack1lll11ll1l1_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1llll111lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11111_opy_,
        bstack1lllll1l1l1_opy_: Tuple[bstack1llll11l11l_opy_, bstack1lll11llll1_opy_],
        *args,
        **kwargs,
    ):
        bstack1llll11111l_opy_ = self.bstack1lll1llll1l_opy_(instance.context)
        if not bstack1llll11111l_opy_:
            self.logger.debug(bstack1l1_opy_ (u"ࠣࡵࡨࡸࡤࡧࡣࡵ࡫ࡹࡩࡤࡶࡡࡨࡧ࠽ࠤࡳࡵࠠࡱࡣࡪࡩࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࠨᄟ") + str(bstack1lllll1l1l1_opy_) + bstack1l1_opy_ (u"ࠤࠥᄠ"))
            return
        f.bstack1llll1l1lll_opy_(instance, bstack1lll1ll1l1l_opy_.bstack1llll1111l1_opy_, bstack1llll11111l_opy_)
    def bstack1lll1llll1l_opy_(self, context: bstack1llll111111_opy_, bstack1lll1ll1ll1_opy_= True):
        if bstack1lll1ll1ll1_opy_:
            bstack1llll11111l_opy_ = self.bstack1lll1llllll_opy_(context, reverse=True)
        else:
            bstack1llll11111l_opy_ = self.bstack1lll11ll1ll_opy_(context, reverse=True)
        return [f for f in bstack1llll11111l_opy_ if f[1].state != bstack1llllll111l_opy_.QUIT]
    def bstack1lll1l11lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11111_opy_,
        bstack1lllll1l1l1_opy_: Tuple[bstack1llll11l11l_opy_, bstack1lll11llll1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1llll111lll_opy_(f, instance, bstack1lllll1l1l1_opy_, *args, **kwargs)
        if not bstack1lll1ll111l_opy_:
            self.logger.debug(bstack1l1_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࡵࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᄡ") + str(kwargs) + bstack1l1_opy_ (u"ࠦࠧᄢ"))
            return
        bstack1llll11111l_opy_ = f.get_state(instance, bstack1lll1ll1l1l_opy_.bstack1llll1111l1_opy_, [])
        if not bstack1llll11111l_opy_:
            self.logger.debug(bstack1l1_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᄣ") + str(kwargs) + bstack1l1_opy_ (u"ࠨࠢᄤ"))
            return
        if len(bstack1llll11111l_opy_) > 1:
            self.logger.debug(
                bstack1lll1llll11_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡾࡰࡪࡴࠨࡱࡣࡪࡩࡤ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳࠪࡿࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࡼ࡭ࡺࡥࡷ࡭ࡳࡾࠤᄥ"))
        bstack1lll1lll11l_opy_, bstack1lll1l1l1l1_opy_ = bstack1llll11111l_opy_[0]
        page = bstack1lll1lll11l_opy_()
        if not page:
            self.logger.debug(bstack1l1_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࠦࡰࡢࡩࡨࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᄦ") + str(kwargs) + bstack1l1_opy_ (u"ࠤࠥᄧ"))
            return
        bstack1lll1ll111_opy_ = getattr(args[0], bstack1l1_opy_ (u"ࠥࡲࡴࡪࡥࡪࡦࠥᄨ"), None)
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack1l1_opy_ (u"ࠦࡹ࡫ࡳࡵࡅࡲࡲࡹ࡫ࡸࡵࡑࡳࡸ࡮ࡵ࡮ࡴࠤᄩ")).get(bstack1l1_opy_ (u"ࠧࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢᄪ")):
            try:
                page.evaluate(bstack1l1_opy_ (u"ࠨ࡟ࠡ࠿ࡁࠤࢀࢃࠢᄫ"),
                            bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡳࡧ࡭ࡦࠤ࠽ࠫᄬ") + json.dumps(
                                bstack1lll1ll111_opy_) + bstack1l1_opy_ (u"ࠣࡿࢀࠦᄭ"))
            except Exception as e:
                self.logger.debug(bstack1l1_opy_ (u"ࠤࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡹࡥࡴࡵ࡬ࡳࡳࠦ࡮ࡢ࡯ࡨࠤࢀࢃࠢᄮ"), e)
    def bstack1lll11ll1l1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11111_opy_,
        bstack1lllll1l1l1_opy_: Tuple[bstack1llll11l11l_opy_, bstack1lll11llll1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1llll111lll_opy_(f, instance, bstack1lllll1l1l1_opy_, *args, **kwargs)
        if not bstack1lll1ll111l_opy_:
            self.logger.debug(bstack1l1_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࡵࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᄯ") + str(kwargs) + bstack1l1_opy_ (u"ࠦࠧᄰ"))
            return
        bstack1llll11111l_opy_ = f.get_state(instance, bstack1lll1ll1l1l_opy_.bstack1llll1111l1_opy_, [])
        if not bstack1llll11111l_opy_:
            self.logger.debug(bstack1l1_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᄱ") + str(kwargs) + bstack1l1_opy_ (u"ࠨࠢᄲ"))
            return
        if len(bstack1llll11111l_opy_) > 1:
            self.logger.debug(
                bstack1lll1llll11_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡾࡰࡪࡴࠨࡱࡣࡪࡩࡤ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳࠪࡿࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࡼ࡭ࡺࡥࡷ࡭ࡳࡾࠤᄳ"))
        bstack1lll1lll11l_opy_, bstack1lll1l1l1l1_opy_ = bstack1llll11111l_opy_[0]
        page = bstack1lll1lll11l_opy_()
        if not page:
            self.logger.debug(bstack1l1_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࠦࡰࡢࡩࡨࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᄴ") + str(kwargs) + bstack1l1_opy_ (u"ࠤࠥᄵ"))
            return
        status = f.get_state(instance, TestFramework.bstack1lll1ll11ll_opy_, None)
        if not status:
            self.logger.debug(bstack1l1_opy_ (u"ࠥࡲࡴࠦࡳࡵࡣࡷࡹࡸࠦࡦࡰࡴࠣࡸࡪࡹࡴ࠭ࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࠨᄶ") + str(bstack1lllll1l1l1_opy_) + bstack1l1_opy_ (u"ࠦࠧᄷ"))
            return
        bstack1lll1l11l11_opy_ = {bstack1l1_opy_ (u"ࠧࡹࡴࡢࡶࡸࡷࠧᄸ"): status.lower()}
        bstack1llll11l111_opy_ = f.get_state(instance, TestFramework.bstack1lll1ll11l1_opy_, None)
        if status.lower() == bstack1l1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᄹ") and bstack1llll11l111_opy_ is not None:
            bstack1lll1l11l11_opy_[bstack1l1_opy_ (u"ࠧࡳࡧࡤࡷࡴࡴࠧᄺ")] = bstack1llll11l111_opy_[0][bstack1l1_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫᄻ")][0] if isinstance(bstack1llll11l111_opy_, list) else str(bstack1llll11l111_opy_)
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack1l1_opy_ (u"ࠤࡷࡩࡸࡺࡃࡰࡰࡷࡩࡽࡺࡏࡱࡶ࡬ࡳࡳࡹࠢᄼ")).get(bstack1l1_opy_ (u"ࠥࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠢᄽ")):
            try:
                page.evaluate(
                        bstack1l1_opy_ (u"ࠦࡤࠦ࠽࠿ࠢࡾࢁࠧᄾ"),
                        bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࠪᄿ")
                        + json.dumps(bstack1lll1l11l11_opy_)
                        + bstack1l1_opy_ (u"ࠨࡽࠣᅀ")
                    )
            except Exception as e:
                self.logger.debug(bstack1l1_opy_ (u"ࠢࡦࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡷࡪࡹࡳࡪࡱࡱࠤࡸࡺࡡࡵࡷࡶࠤࢀࢃࠢᅁ"), e)
    def bstack1lll1lll1ll_opy_(
        self,
        instance: bstack1lll1l11111_opy_,
        f: TestFramework,
        bstack1lllll1l1l1_opy_: Tuple[bstack1llll11l11l_opy_, bstack1lll11llll1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1llll111lll_opy_(f, instance, bstack1lllll1l1l1_opy_, *args, **kwargs)
        if not bstack1lll1ll111l_opy_:
            self.logger.debug(
                bstack1lll1llll11_opy_ (u"ࠣ࡯ࡤࡶࡰࡥ࡯࠲࠳ࡼࡣࡸࡿ࡮ࡤ࠼ࠣࡲࡴࡺࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠬࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࡼ࡭ࡺࡥࡷ࡭ࡳࡾࠤᅂ"))
            return
        bstack1llll11111l_opy_ = f.get_state(instance, bstack1lll1ll1l1l_opy_.bstack1llll1111l1_opy_, [])
        if not bstack1llll11111l_opy_:
            self.logger.debug(bstack1l1_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᅃ") + str(kwargs) + bstack1l1_opy_ (u"ࠥࠦᅄ"))
            return
        if len(bstack1llll11111l_opy_) > 1:
            self.logger.debug(
                bstack1lll1llll11_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦࡻ࡭ࡧࡱࠬࡵࡧࡧࡦࡡ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷ࠮ࢃࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࢀࡱࡷࡢࡴࡪࡷࢂࠨᅅ"))
        bstack1lll1lll11l_opy_, bstack1lll1l1l1l1_opy_ = bstack1llll11111l_opy_[0]
        page = bstack1lll1lll11l_opy_()
        if not page:
            self.logger.debug(bstack1l1_opy_ (u"ࠧࡳࡡࡳ࡭ࡢࡳ࠶࠷ࡹࡠࡵࡼࡲࡨࡀࠠ࡯ࡱࠣࡴࡦ࡭ࡥࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᅆ") + str(kwargs) + bstack1l1_opy_ (u"ࠨࠢᅇ"))
            return
        timestamp = int(time.time() * 1000)
        data = bstack1l1_opy_ (u"ࠢࡐࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࡓࡺࡰࡦ࠾ࠧᅈ") + str(timestamp)
        try:
            page.evaluate(
                bstack1l1_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤᅉ"),
                bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࢃࠧᅊ").format(
                    json.dumps(
                        {
                            bstack1l1_opy_ (u"ࠥࡥࡨࡺࡩࡰࡰࠥᅋ"): bstack1l1_opy_ (u"ࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨᅌ"),
                            bstack1l1_opy_ (u"ࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣᅍ"): {
                                bstack1l1_opy_ (u"ࠨࡴࡺࡲࡨࠦᅎ"): bstack1l1_opy_ (u"ࠢࡂࡰࡱࡳࡹࡧࡴࡪࡱࡱࠦᅏ"),
                                bstack1l1_opy_ (u"ࠣࡦࡤࡸࡦࠨᅐ"): data,
                                bstack1l1_opy_ (u"ࠤ࡯ࡩࡻ࡫࡬ࠣᅑ"): bstack1l1_opy_ (u"ࠥࡨࡪࡨࡵࡨࠤᅒ")
                            }
                        }
                    )
                )
            )
        except Exception as e:
            self.logger.debug(bstack1l1_opy_ (u"ࠦࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡰ࠳࠴ࡽࠥࡧ࡮࡯ࡱࡷࡥࡹ࡯࡯࡯ࠢࡰࡥࡷࡱࡩ࡯ࡩࠣࡿࢂࠨᅓ"), e)
    def bstack1lll1ll1lll_opy_(
        self,
        instance: bstack1lll1l11111_opy_,
        f: TestFramework,
        bstack1lllll1l1l1_opy_: Tuple[bstack1llll11l11l_opy_, bstack1lll11llll1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1llll111lll_opy_(f, instance, bstack1lllll1l1l1_opy_, *args, **kwargs)
        if f.get_state(instance, bstack1lll1ll1l1l_opy_.bstack1lll1l111ll_opy_, False):
            return
        self.bstack1llll1l1l1l_opy_()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1lllll1l11l_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1lll1l1111l_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll1ll1l11_opy_)
        req.test_framework_state = bstack1lllll1l1l1_opy_[0].name
        req.test_hook_state = bstack1lllll1l1l1_opy_[1].name
        req.test_uuid = TestFramework.get_state(instance, TestFramework.bstack1llll111ll1_opy_)
        for bstack1lll1l1lll1_opy_ in bstack1llll111l11_opy_.bstack1lll1lllll1_opy_.values():
            session = req.automation_sessions.add()
            session.provider = (
                bstack1l1_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠦᅔ")
                if bstack1lll1ll111l_opy_
                else bstack1l1_opy_ (u"ࠨࡵ࡯࡭ࡱࡳࡼࡴ࡟ࡨࡴ࡬ࡨࠧᅕ")
            )
            session.ref = bstack1lll1l1lll1_opy_.ref()
            session.hub_url = bstack1llll111l11_opy_.get_state(bstack1lll1l1lll1_opy_, bstack1llll111l11_opy_.bstack1lll1l1l11l_opy_, bstack1l1_opy_ (u"ࠢࠣᅖ"))
            session.framework_name = bstack1lll1l1lll1_opy_.framework_name
            session.framework_version = bstack1lll1l1lll1_opy_.framework_version
            session.framework_session_id = bstack1llll111l11_opy_.get_state(bstack1lll1l1lll1_opy_, bstack1llll111l11_opy_.bstack1lll11ll11l_opy_, bstack1l1_opy_ (u"ࠣࠤᅗ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1lll1l1ll1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11111_opy_,
        bstack1lllll1l1l1_opy_: Tuple[bstack1llll11l11l_opy_, bstack1lll11llll1_opy_],
        *args,
        **kwargs
    ):
        bstack1llll11111l_opy_ = f.get_state(instance, bstack1lll1ll1l1l_opy_.bstack1llll1111l1_opy_, [])
        if not bstack1llll11111l_opy_:
            self.logger.debug(bstack1l1_opy_ (u"ࠤࡪࡩࡹࡥࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡨࡷ࡯ࡶࡦࡴ࠽ࠤࡳࡵࠠࡱࡣࡪࡩࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᅘ") + str(kwargs) + bstack1l1_opy_ (u"ࠥࠦᅙ"))
            return
        if len(bstack1llll11111l_opy_) > 1:
            self.logger.debug(bstack1l1_opy_ (u"ࠦ࡬࡫ࡴࡠࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡪࡲࡪࡸࡨࡶ࠿ࠦࡻ࡭ࡧࡱࠬࡵࡧࡧࡦࡡ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷ࠮ࢃࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᅚ") + str(kwargs) + bstack1l1_opy_ (u"ࠧࠨᅛ"))
        bstack1lll1lll11l_opy_, bstack1lll1l1l1l1_opy_ = bstack1llll11111l_opy_[0]
        page = bstack1lll1lll11l_opy_()
        if not page:
            self.logger.debug(bstack1l1_opy_ (u"ࠨࡧࡦࡶࡢࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡥࡴ࡬ࡺࡪࡸ࠺ࠡࡰࡲࠤࡵࡧࡧࡦࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᅜ") + str(kwargs) + bstack1l1_opy_ (u"ࠢࠣᅝ"))
            return
        return page
    def bstack1lll1l11l1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11111_opy_,
        bstack1lllll1l1l1_opy_: Tuple[bstack1llll11l11l_opy_, bstack1lll11llll1_opy_],
        *args,
        **kwargs
    ):
        caps = {}
        bstack1llll111l1l_opy_ = {}
        for bstack1lll1l1lll1_opy_ in bstack1llll111l11_opy_.bstack1lll1lllll1_opy_.values():
            caps = bstack1llll111l11_opy_.get_state(bstack1lll1l1lll1_opy_, bstack1llll111l11_opy_.bstack1lll11lll11_opy_, bstack1l1_opy_ (u"ࠣࠤᅞ"))
        bstack1llll111l1l_opy_[bstack1l1_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠢᅟ")] = caps.get(bstack1l1_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࠦᅠ"), bstack1l1_opy_ (u"ࠦࠧᅡ"))
        bstack1llll111l1l_opy_[bstack1l1_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠦᅢ")] = caps.get(bstack1l1_opy_ (u"ࠨ࡯ࡴࠤᅣ"), bstack1l1_opy_ (u"ࠢࠣᅤ"))
        bstack1llll111l1l_opy_[bstack1l1_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠥᅥ")] = caps.get(bstack1l1_opy_ (u"ࠤࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳࠨᅦ"), bstack1l1_opy_ (u"ࠥࠦᅧ"))
        bstack1llll111l1l_opy_[bstack1l1_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠧᅨ")] = caps.get(bstack1l1_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠢᅩ"), bstack1l1_opy_ (u"ࠨࠢᅪ"))
        return bstack1llll111l1l_opy_
    def bstack1lll1lll1l1_opy_(self, page: object, bstack1lll1l1l111_opy_, args={}):
        try:
            bstack1llll11l1ll_opy_ = bstack1l1_opy_ (u"ࠢࠣࠤࠫࡪࡺࡴࡣࡵ࡫ࡲࡲࠥ࠮࠮࠯࠰ࡥࡷࡹࡧࡣ࡬ࡕࡧ࡯ࡆࡸࡧࡴࠫࠣࡿࢀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡴࡨࡸࡺࡸ࡮ࠡࡰࡨࡻࠥࡖࡲࡰ࡯࡬ࡷࡪ࠮ࠨࡳࡧࡶࡳࡱࡼࡥ࠭ࠢࡵࡩ࡯࡫ࡣࡵࠫࠣࡁࡃࠦࡻࡼࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡤࡶࡸࡦࡩ࡫ࡔࡦ࡮ࡅࡷ࡭ࡳ࠯ࡲࡸࡷ࡭࠮ࡲࡦࡵࡲࡰࡻ࡫ࠩ࠼ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡽࡩࡲࡤࡨ࡯ࡥࡻࢀࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡽࡾࠫ࠾ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࢀࢁ࠮࠮ࡻࡢࡴࡪࡣ࡯ࡹ࡯࡯ࡿࠬࠦࠧࠨᅫ")
            bstack1lll1l1l111_opy_ = bstack1lll1l1l111_opy_.replace(bstack1l1_opy_ (u"ࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦᅬ"), bstack1l1_opy_ (u"ࠤࡥࡷࡹࡧࡣ࡬ࡕࡧ࡯ࡆࡸࡧࡴࠤᅭ"))
            script = bstack1llll11l1ll_opy_.format(fn_body=bstack1lll1l1l111_opy_, arg_json=json.dumps(args))
            return page.evaluate(script)
        except Exception as e:
            self.logger.error(bstack1l1_opy_ (u"ࠥࡥ࠶࠷ࡹࡠࡵࡦࡶ࡮ࡶࡴࡠࡧࡻࡩࡨࡻࡴࡦ࠼ࠣࡉࡷࡸ࡯ࡳࠢࡨࡼࡪࡩࡵࡵ࡫ࡱ࡫ࠥࡺࡨࡦࠢࡤ࠵࠶ࡿࠠࡴࡥࡵ࡭ࡵࡺࠬࠡࠤᅮ") + str(e) + bstack1l1_opy_ (u"ࠦࠧᅯ"))