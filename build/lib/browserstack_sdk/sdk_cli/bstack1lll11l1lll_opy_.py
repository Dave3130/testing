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
import json
import time
import os
import threading
import asyncio
from browserstack_sdk.sdk_cli.bstack1lllll1ll1l_opy_ import (
    bstack1lllll111ll_opy_,
    bstack1llllll1l11_opy_,
    bstack1llll11l11l_opy_,
    bstack1lll11l1ll1_opy_,
)
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1lll1l11111_opy_, bstack1lll1ll11l_opy_
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import bstack1lllll1l11l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l1ll11_opy_, bstack1llll11l111_opy_, bstack1llll11111l_opy_
from browserstack_sdk.sdk_cli.bstack1lll1lll1ll_opy_ import bstack1lll1l1l1l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1llll1l_opy_ import bstack1lll11ll1l1_opy_
from typing import Tuple, List, Any
from bstack_utils.bstack1111ll1lll_opy_ import bstack11l111111l_opy_, bstack1lllll1l1l_opy_, bstack1l1lll111l_opy_
from browserstack_sdk import sdk_pb2 as structs
class bstack1lll11ll11l_opy_(bstack1lll11ll1l1_opy_):
    bstack1lll1l1111l_opy_ = bstack11lll1_opy_ (u"ࠢࡵࡧࡶࡸࡤࡪࡲࡪࡸࡨࡶࡸࠨᄞ")
    bstack1llll111ll1_opy_ = bstack11lll1_opy_ (u"ࠣࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡹࡥࡴࡵ࡬ࡳࡳࡹࠢᄟ")
    bstack1lll1l1llll_opy_ = bstack11lll1_opy_ (u"ࠤࡱࡳࡳࡥࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡶࡩࡸࡹࡩࡰࡰࡶࠦᄠ")
    bstack1lll1ll1l11_opy_ = bstack11lll1_opy_ (u"ࠥࡸࡪࡹࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡵࠥᄡ")
    bstack1lll1lll1l1_opy_ = bstack11lll1_opy_ (u"ࠦࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡢࡶࡪ࡬ࡳࠣᄢ")
    bstack1lll1l111ll_opy_ = bstack11lll1_opy_ (u"ࠧࡩࡢࡵࡡࡶࡩࡸࡹࡩࡰࡰࡢࡧࡷ࡫ࡡࡵࡧࡧࠦᄣ")
    bstack1lll1l11l1l_opy_ = bstack11lll1_opy_ (u"ࠨࡣࡣࡶࡢࡷࡪࡹࡳࡪࡱࡱࡣࡳࡧ࡭ࡦࠤᄤ")
    bstack1lll1ll1lll_opy_ = bstack11lll1_opy_ (u"ࠢࡤࡤࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡹࡴࡢࡶࡸࡷࠧᄥ")
    def __init__(self):
        super().__init__(bstack1llll111l1l_opy_=self.bstack1lll1l1111l_opy_, frameworks=[bstack1lllll1l11l_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1lllll1llll_opy_((bstack1lll1l1ll11_opy_.BEFORE_EACH, bstack1llll11l111_opy_.POST), self.bstack1llll111111_opy_)
        if bstack1lll1ll11l_opy_():
            TestFramework.bstack1lllll1llll_opy_((bstack1lll1l1ll11_opy_.TEST, bstack1llll11l111_opy_.POST), self.bstack1lll1l11lll_opy_)
        else:
            TestFramework.bstack1lllll1llll_opy_((bstack1lll1l1ll11_opy_.TEST, bstack1llll11l111_opy_.PRE), self.bstack1lll1l11lll_opy_)
        TestFramework.bstack1lllll1llll_opy_((bstack1lll1l1ll11_opy_.TEST, bstack1llll11l111_opy_.POST), self.bstack1lll11lll1l_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1llll111111_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll11111l_opy_,
        bstack1llll1lll1l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1llll11l111_opy_],
        *args,
        **kwargs,
    ):
        bstack1lll1ll1l1l_opy_ = self.bstack1llll111l11_opy_(instance.context)
        if not bstack1lll1ll1l1l_opy_:
            self.logger.debug(bstack11lll1_opy_ (u"ࠣࡵࡨࡸࡤࡧࡣࡵ࡫ࡹࡩࡤࡶࡡࡨࡧ࠽ࠤࡳࡵࠠࡱࡣࡪࡩࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࠨᄦ") + str(bstack1llll1lll1l_opy_) + bstack11lll1_opy_ (u"ࠤࠥᄧ"))
            return
        f.bstack1lllll11l11_opy_(instance, bstack1lll11ll11l_opy_.bstack1llll111ll1_opy_, bstack1lll1ll1l1l_opy_)
    def bstack1llll111l11_opy_(self, context: bstack1lll11l1ll1_opy_, bstack1lll1l111l1_opy_= True):
        if bstack1lll1l111l1_opy_:
            bstack1lll1ll1l1l_opy_ = self.bstack1lll1l1ll1l_opy_(context, reverse=True)
        else:
            bstack1lll1ll1l1l_opy_ = self.bstack1lll1lll11l_opy_(context, reverse=True)
        return [f for f in bstack1lll1ll1l1l_opy_ if f[1].state != bstack1lllll111ll_opy_.QUIT]
    def bstack1lll1l11lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll11111l_opy_,
        bstack1llll1lll1l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1llll11l111_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1llll111111_opy_(f, instance, bstack1llll1lll1l_opy_, *args, **kwargs)
        if not bstack1lll1l11111_opy_:
            self.logger.debug(bstack11lll1_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࡵࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᄨ") + str(kwargs) + bstack11lll1_opy_ (u"ࠦࠧᄩ"))
            return
        bstack1lll1ll1l1l_opy_ = f.get_state(instance, bstack1lll11ll11l_opy_.bstack1llll111ll1_opy_, [])
        if not bstack1lll1ll1l1l_opy_:
            self.logger.debug(bstack11lll1_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᄪ") + str(kwargs) + bstack11lll1_opy_ (u"ࠨࠢᄫ"))
            return
        if len(bstack1lll1ll1l1l_opy_) > 1:
            self.logger.debug(
                bstack1lll1ll1111_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡾࡰࡪࡴࠨࡱࡣࡪࡩࡤ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳࠪࡿࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࡼ࡭ࡺࡥࡷ࡭ࡳࡾࠤᄬ"))
        bstack1lll11lll11_opy_, bstack1lll1llll11_opy_ = bstack1lll1ll1l1l_opy_[0]
        page = bstack1lll11lll11_opy_()
        if not page:
            self.logger.debug(bstack11lll1_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࠦࡰࡢࡩࡨࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᄭ") + str(kwargs) + bstack11lll1_opy_ (u"ࠤࠥᄮ"))
            return
        bstack1lll11l1l1_opy_ = getattr(args[0], bstack11lll1_opy_ (u"ࠥࡲࡴࡪࡥࡪࡦࠥᄯ"), None)
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack11lll1_opy_ (u"ࠦࡹ࡫ࡳࡵࡅࡲࡲࡹ࡫ࡸࡵࡑࡳࡸ࡮ࡵ࡮ࡴࠤᄰ")).get(bstack11lll1_opy_ (u"ࠧࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢᄱ")):
            try:
                page.evaluate(bstack11lll1_opy_ (u"ࠨ࡟ࠡ࠿ࡁࠤࢀࢃࠢᄲ"),
                            bstack11lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡳࡧ࡭ࡦࠤ࠽ࠫᄳ") + json.dumps(
                                bstack1lll11l1l1_opy_) + bstack11lll1_opy_ (u"ࠣࡿࢀࠦᄴ"))
            except Exception as e:
                self.logger.debug(bstack11lll1_opy_ (u"ࠤࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡹࡥࡴࡵ࡬ࡳࡳࠦ࡮ࡢ࡯ࡨࠤࢀࢃࠢᄵ"), e)
    def bstack1lll11lll1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll11111l_opy_,
        bstack1llll1lll1l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1llll11l111_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1llll111111_opy_(f, instance, bstack1llll1lll1l_opy_, *args, **kwargs)
        if not bstack1lll1l11111_opy_:
            self.logger.debug(bstack11lll1_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࡵࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᄶ") + str(kwargs) + bstack11lll1_opy_ (u"ࠦࠧᄷ"))
            return
        bstack1lll1ll1l1l_opy_ = f.get_state(instance, bstack1lll11ll11l_opy_.bstack1llll111ll1_opy_, [])
        if not bstack1lll1ll1l1l_opy_:
            self.logger.debug(bstack11lll1_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᄸ") + str(kwargs) + bstack11lll1_opy_ (u"ࠨࠢᄹ"))
            return
        if len(bstack1lll1ll1l1l_opy_) > 1:
            self.logger.debug(
                bstack1lll1ll1111_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡾࡰࡪࡴࠨࡱࡣࡪࡩࡤ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳࠪࡿࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࡼ࡭ࡺࡥࡷ࡭ࡳࡾࠤᄺ"))
        bstack1lll11lll11_opy_, bstack1lll1llll11_opy_ = bstack1lll1ll1l1l_opy_[0]
        page = bstack1lll11lll11_opy_()
        if not page:
            self.logger.debug(bstack11lll1_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࠦࡰࡢࡩࡨࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᄻ") + str(kwargs) + bstack11lll1_opy_ (u"ࠤࠥᄼ"))
            return
        status = f.get_state(instance, TestFramework.bstack1lll1ll111l_opy_, None)
        if not status:
            self.logger.debug(bstack11lll1_opy_ (u"ࠥࡲࡴࠦࡳࡵࡣࡷࡹࡸࠦࡦࡰࡴࠣࡸࡪࡹࡴ࠭ࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࠨᄽ") + str(bstack1llll1lll1l_opy_) + bstack11lll1_opy_ (u"ࠦࠧᄾ"))
            return
        bstack1lll1lll111_opy_ = {bstack11lll1_opy_ (u"ࠧࡹࡴࡢࡶࡸࡷࠧᄿ"): status.lower()}
        bstack1lll11lllll_opy_ = f.get_state(instance, TestFramework.bstack1lll1l1lll1_opy_, None)
        if status.lower() == bstack11lll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᅀ") and bstack1lll11lllll_opy_ is not None:
            bstack1lll1lll111_opy_[bstack11lll1_opy_ (u"ࠧࡳࡧࡤࡷࡴࡴࠧᅁ")] = bstack1lll11lllll_opy_[0][bstack11lll1_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫᅂ")][0] if isinstance(bstack1lll11lllll_opy_, list) else str(bstack1lll11lllll_opy_)
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack11lll1_opy_ (u"ࠤࡷࡩࡸࡺࡃࡰࡰࡷࡩࡽࡺࡏࡱࡶ࡬ࡳࡳࡹࠢᅃ")).get(bstack11lll1_opy_ (u"ࠥࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠢᅄ")):
            try:
                page.evaluate(
                        bstack11lll1_opy_ (u"ࠦࡤࠦ࠽࠿ࠢࡾࢁࠧᅅ"),
                        bstack11lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࠪᅆ")
                        + json.dumps(bstack1lll1lll111_opy_)
                        + bstack11lll1_opy_ (u"ࠨࡽࠣᅇ")
                    )
            except Exception as e:
                self.logger.debug(bstack11lll1_opy_ (u"ࠢࡦࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡷࡪࡹࡳࡪࡱࡱࠤࡸࡺࡡࡵࡷࡶࠤࢀࢃࠢᅈ"), e)
    def bstack1lll11llll1_opy_(
        self,
        instance: bstack1llll11111l_opy_,
        f: TestFramework,
        bstack1llll1lll1l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1llll11l111_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1llll111111_opy_(f, instance, bstack1llll1lll1l_opy_, *args, **kwargs)
        if not bstack1lll1l11111_opy_:
            self.logger.debug(
                bstack1lll1ll1111_opy_ (u"ࠣ࡯ࡤࡶࡰࡥ࡯࠲࠳ࡼࡣࡸࡿ࡮ࡤ࠼ࠣࡲࡴࡺࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠬࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࡼ࡭ࡺࡥࡷ࡭ࡳࡾࠤᅉ"))
            return
        bstack1lll1ll1l1l_opy_ = f.get_state(instance, bstack1lll11ll11l_opy_.bstack1llll111ll1_opy_, [])
        if not bstack1lll1ll1l1l_opy_:
            self.logger.debug(bstack11lll1_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᅊ") + str(kwargs) + bstack11lll1_opy_ (u"ࠥࠦᅋ"))
            return
        if len(bstack1lll1ll1l1l_opy_) > 1:
            self.logger.debug(
                bstack1lll1ll1111_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦࡻ࡭ࡧࡱࠬࡵࡧࡧࡦࡡ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷ࠮ࢃࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࢀࡱࡷࡢࡴࡪࡷࢂࠨᅌ"))
        bstack1lll11lll11_opy_, bstack1lll1llll11_opy_ = bstack1lll1ll1l1l_opy_[0]
        page = bstack1lll11lll11_opy_()
        if not page:
            self.logger.debug(bstack11lll1_opy_ (u"ࠧࡳࡡࡳ࡭ࡢࡳ࠶࠷ࡹࡠࡵࡼࡲࡨࡀࠠ࡯ࡱࠣࡴࡦ࡭ࡥࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᅍ") + str(kwargs) + bstack11lll1_opy_ (u"ࠨࠢᅎ"))
            return
        timestamp = int(time.time() * 1000)
        data = bstack11lll1_opy_ (u"ࠢࡐࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࡓࡺࡰࡦ࠾ࠧᅏ") + str(timestamp)
        try:
            page.evaluate(
                bstack11lll1_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤᅐ"),
                bstack11lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࢃࠧᅑ").format(
                    json.dumps(
                        {
                            bstack11lll1_opy_ (u"ࠥࡥࡨࡺࡩࡰࡰࠥᅒ"): bstack11lll1_opy_ (u"ࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨᅓ"),
                            bstack11lll1_opy_ (u"ࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣᅔ"): {
                                bstack11lll1_opy_ (u"ࠨࡴࡺࡲࡨࠦᅕ"): bstack11lll1_opy_ (u"ࠢࡂࡰࡱࡳࡹࡧࡴࡪࡱࡱࠦᅖ"),
                                bstack11lll1_opy_ (u"ࠣࡦࡤࡸࡦࠨᅗ"): data,
                                bstack11lll1_opy_ (u"ࠤ࡯ࡩࡻ࡫࡬ࠣᅘ"): bstack11lll1_opy_ (u"ࠥࡨࡪࡨࡵࡨࠤᅙ")
                            }
                        }
                    )
                )
            )
        except Exception as e:
            self.logger.debug(bstack11lll1_opy_ (u"ࠦࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡰ࠳࠴ࡽࠥࡧ࡮࡯ࡱࡷࡥࡹ࡯࡯࡯ࠢࡰࡥࡷࡱࡩ࡯ࡩࠣࡿࢂࠨᅚ"), e)
    def bstack1lll1ll1ll1_opy_(
        self,
        instance: bstack1llll11111l_opy_,
        f: TestFramework,
        bstack1llll1lll1l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1llll11l111_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1llll111111_opy_(f, instance, bstack1llll1lll1l_opy_, *args, **kwargs)
        if f.get_state(instance, bstack1lll11ll11l_opy_.bstack1lll1l111ll_opy_, False):
            return
        self.bstack1llll1ll1ll_opy_()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1llll1ll111_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1lll1l11l11_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll1ll11ll_opy_)
        req.test_framework_state = bstack1llll1lll1l_opy_[0].name
        req.test_hook_state = bstack1llll1lll1l_opy_[1].name
        req.test_uuid = TestFramework.get_state(instance, TestFramework.bstack1lll11ll111_opy_)
        for bstack1llll111lll_opy_ in bstack1lll1l1l1l1_opy_.bstack1lll1lllll1_opy_.values():
            session = req.automation_sessions.add()
            session.provider = (
                bstack11lll1_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠦᅛ")
                if bstack1lll1l11111_opy_
                else bstack11lll1_opy_ (u"ࠨࡵ࡯࡭ࡱࡳࡼࡴ࡟ࡨࡴ࡬ࡨࠧᅜ")
            )
            session.ref = bstack1llll111lll_opy_.ref()
            session.hub_url = bstack1lll1l1l1l1_opy_.get_state(bstack1llll111lll_opy_, bstack1lll1l1l1l1_opy_.bstack1lll1l1l11l_opy_, bstack11lll1_opy_ (u"ࠢࠣᅝ"))
            session.framework_name = bstack1llll111lll_opy_.framework_name
            session.framework_version = bstack1llll111lll_opy_.framework_version
            session.framework_session_id = bstack1lll1l1l1l1_opy_.get_state(bstack1llll111lll_opy_, bstack1lll1l1l1l1_opy_.bstack1lll1l1l1ll_opy_, bstack11lll1_opy_ (u"ࠣࠤᅞ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1lll1ll11l1_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll11111l_opy_,
        bstack1llll1lll1l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1llll11l111_opy_],
        *args,
        **kwargs
    ):
        bstack1lll1ll1l1l_opy_ = f.get_state(instance, bstack1lll11ll11l_opy_.bstack1llll111ll1_opy_, [])
        if not bstack1lll1ll1l1l_opy_:
            self.logger.debug(bstack11lll1_opy_ (u"ࠤࡪࡩࡹࡥࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡨࡷ࡯ࡶࡦࡴ࠽ࠤࡳࡵࠠࡱࡣࡪࡩࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᅟ") + str(kwargs) + bstack11lll1_opy_ (u"ࠥࠦᅠ"))
            return
        if len(bstack1lll1ll1l1l_opy_) > 1:
            self.logger.debug(bstack11lll1_opy_ (u"ࠦ࡬࡫ࡴࡠࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡪࡲࡪࡸࡨࡶ࠿ࠦࡻ࡭ࡧࡱࠬࡵࡧࡧࡦࡡ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷ࠮ࢃࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᅡ") + str(kwargs) + bstack11lll1_opy_ (u"ࠧࠨᅢ"))
        bstack1lll11lll11_opy_, bstack1lll1llll11_opy_ = bstack1lll1ll1l1l_opy_[0]
        page = bstack1lll11lll11_opy_()
        if not page:
            self.logger.debug(bstack11lll1_opy_ (u"ࠨࡧࡦࡶࡢࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡥࡴ࡬ࡺࡪࡸ࠺ࠡࡰࡲࠤࡵࡧࡧࡦࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᅣ") + str(kwargs) + bstack11lll1_opy_ (u"ࠢࠣᅤ"))
            return
        return page
    def bstack1lll1l11ll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll11111l_opy_,
        bstack1llll1lll1l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1llll11l111_opy_],
        *args,
        **kwargs
    ):
        caps = {}
        bstack1lll1llllll_opy_ = {}
        for bstack1llll111lll_opy_ in bstack1lll1l1l1l1_opy_.bstack1lll1lllll1_opy_.values():
            caps = bstack1lll1l1l1l1_opy_.get_state(bstack1llll111lll_opy_, bstack1lll1l1l1l1_opy_.bstack1lll11ll1ll_opy_, bstack11lll1_opy_ (u"ࠣࠤᅥ"))
        bstack1lll1llllll_opy_[bstack11lll1_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠢᅦ")] = caps.get(bstack11lll1_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࠦᅧ"), bstack11lll1_opy_ (u"ࠦࠧᅨ"))
        bstack1lll1llllll_opy_[bstack11lll1_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠦᅩ")] = caps.get(bstack11lll1_opy_ (u"ࠨ࡯ࡴࠤᅪ"), bstack11lll1_opy_ (u"ࠢࠣᅫ"))
        bstack1lll1llllll_opy_[bstack11lll1_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠥᅬ")] = caps.get(bstack11lll1_opy_ (u"ࠤࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳࠨᅭ"), bstack11lll1_opy_ (u"ࠥࠦᅮ"))
        bstack1lll1llllll_opy_[bstack11lll1_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠧᅯ")] = caps.get(bstack11lll1_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠢᅰ"), bstack11lll1_opy_ (u"ࠨࠢᅱ"))
        return bstack1lll1llllll_opy_
    def bstack1llll1111l1_opy_(self, page: object, bstack1lll1l1l111_opy_, args={}):
        try:
            bstack1llll1111ll_opy_ = bstack11lll1_opy_ (u"ࠢࠣࠤࠫࡪࡺࡴࡣࡵ࡫ࡲࡲࠥ࠮࠮࠯࠰ࡥࡷࡹࡧࡣ࡬ࡕࡧ࡯ࡆࡸࡧࡴࠫࠣࡿࢀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡴࡨࡸࡺࡸ࡮ࠡࡰࡨࡻࠥࡖࡲࡰ࡯࡬ࡷࡪ࠮ࠨࡳࡧࡶࡳࡱࡼࡥ࠭ࠢࡵࡩ࡯࡫ࡣࡵࠫࠣࡁࡃࠦࡻࡼࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡤࡶࡸࡦࡩ࡫ࡔࡦ࡮ࡅࡷ࡭ࡳ࠯ࡲࡸࡷ࡭࠮ࡲࡦࡵࡲࡰࡻ࡫ࠩ࠼ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡽࡩࡲࡤࡨ࡯ࡥࡻࢀࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡽࡾࠫ࠾ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࢀࢁ࠮࠮ࡻࡢࡴࡪࡣ࡯ࡹ࡯࡯ࡿࠬࠦࠧࠨᅲ")
            bstack1lll1l1l111_opy_ = bstack1lll1l1l111_opy_.replace(bstack11lll1_opy_ (u"ࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦᅳ"), bstack11lll1_opy_ (u"ࠤࡥࡷࡹࡧࡣ࡬ࡕࡧ࡯ࡆࡸࡧࡴࠤᅴ"))
            script = bstack1llll1111ll_opy_.format(fn_body=bstack1lll1l1l111_opy_, arg_json=json.dumps(args))
            return page.evaluate(script)
        except Exception as e:
            self.logger.error(bstack11lll1_opy_ (u"ࠥࡥ࠶࠷ࡹࡠࡵࡦࡶ࡮ࡶࡴࡠࡧࡻࡩࡨࡻࡴࡦ࠼ࠣࡉࡷࡸ࡯ࡳࠢࡨࡼࡪࡩࡵࡵ࡫ࡱ࡫ࠥࡺࡨࡦࠢࡤ࠵࠶ࡿࠠࡴࡥࡵ࡭ࡵࡺࠬࠡࠤᅵ") + str(e) + bstack11lll1_opy_ (u"ࠦࠧᅶ"))