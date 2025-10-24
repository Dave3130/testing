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
import sys
import logging
import tarfile
import io
import os
import time
import requests
import re
from requests_toolbelt.multipart.encoder import MultipartEncoder
from bstack_utils.constants import bstack11l1l11111l_opy_, bstack11l1l1l111l_opy_, bstack11l11l1llll_opy_
import tempfile
import json
bstack11111l1llll_opy_ = os.getenv(bstack1l1_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡌࡐࡉࡢࡊࡎࡒࡅࠣẼ"), None) or os.path.join(tempfile.gettempdir(), bstack1l1_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡥࡧࡥࡹ࡬࠴࡬ࡰࡩࠥẽ"))
bstack11111l11l11_opy_ = os.path.join(bstack1l1_opy_ (u"ࠤ࡯ࡳ࡬ࠨẾ"), bstack1l1_opy_ (u"ࠪࡷࡩࡱ࠭ࡤ࡮࡬࠱ࡩ࡫ࡢࡶࡩ࠱ࡰࡴ࡭ࠧế"))
logging.Formatter.converter = time.gmtime
def get_logger(name=__name__, level=None):
  logger = logging.getLogger(name)
  if level:
    logging.basicConfig(
      level=level,
      format=bstack1l1_opy_ (u"ࠫࠪ࠮ࡡࡴࡥࡷ࡭ࡲ࡫ࠩࡴࠢ࡞ࠩ࠭ࡴࡡ࡮ࡧࠬࡷࡢࡡࠥࠩ࡮ࡨࡺࡪࡲ࡮ࡢ࡯ࡨ࠭ࡸࡣࠠ࠮ࠢࠨࠬࡲ࡫ࡳࡴࡣࡪࡩ࠮ࡹࠧỀ"),
      datefmt=bstack1l1_opy_ (u"࡙ࠬࠫ࠮ࠧࡰ࠱ࠪࡪࡔࠦࡊ࠽ࠩࡒࡀࠥࡔ࡜ࠪề"),
      stream=sys.stdout
    )
  return logger
def bstack1l1l111l1ll_opy_():
  bstack11111l1l1ll_opy_ = os.environ.get(bstack1l1_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡈࡉࡏࡃࡕ࡝ࡤࡊࡅࡃࡗࡊࠦỂ"), bstack1l1_opy_ (u"ࠢࡧࡣ࡯ࡷࡪࠨể"))
  return logging.DEBUG if bstack11111l1l1ll_opy_.lower() == bstack1l1_opy_ (u"ࠣࡶࡵࡹࡪࠨỄ") else logging.INFO
def bstack1ll1l1l1l11_opy_():
  global bstack11111l1llll_opy_
  if os.path.exists(bstack11111l1llll_opy_):
    os.remove(bstack11111l1llll_opy_)
  if os.path.exists(bstack11111l11l11_opy_):
    os.remove(bstack11111l11l11_opy_)
def bstack1l1111l1ll_opy_():
  for handler in logging.getLogger().handlers:
    logging.getLogger().removeHandler(handler)
def configure_logger(config, log_level):
  bstack11111l11lll_opy_ = log_level
  if bstack1l1_opy_ (u"ࠩ࡯ࡳ࡬ࡒࡥࡷࡧ࡯ࠫễ") in config and config[bstack1l1_opy_ (u"ࠪࡰࡴ࡭ࡌࡦࡸࡨࡰࠬỆ")] in bstack11l1l1l111l_opy_:
    bstack11111l11lll_opy_ = bstack11l1l1l111l_opy_[config[bstack1l1_opy_ (u"ࠫࡱࡵࡧࡍࡧࡹࡩࡱ࠭ệ")]]
  if config.get(bstack1l1_opy_ (u"ࠬࡪࡩࡴࡣࡥࡰࡪࡇࡵࡵࡱࡆࡥࡵࡺࡵࡳࡧࡏࡳ࡬ࡹࠧỈ"), False):
    logging.getLogger().setLevel(bstack11111l11lll_opy_)
    return bstack11111l11lll_opy_
  global bstack11111l1llll_opy_
  bstack1l1111l1ll_opy_()
  bstack11111ll1lll_opy_ = logging.Formatter(
    fmt=bstack1l1_opy_ (u"࠭ࠥࠩࡣࡶࡧࡹ࡯࡭ࡦࠫࡶࠤࡠࠫࠨ࡯ࡣࡰࡩ࠮ࡹ࡝࡜ࠧࠫࡰࡪࡼࡥ࡭ࡰࡤࡱࡪ࠯ࡳ࡞ࠢ࠰ࠤࠪ࠮࡭ࡦࡵࡶࡥ࡬࡫ࠩࡴࠩỉ"),
    datefmt=bstack1l1_opy_ (u"࡛ࠧࠦ࠰ࠩࡲ࠳ࠥࡥࡖࠨࡌ࠿ࠫࡍ࠻ࠧࡖ࡞ࠬỊ"),
  )
  bstack11111l11ll1_opy_ = logging.StreamHandler(sys.stdout)
  file_handler = logging.FileHandler(bstack11111l1llll_opy_)
  file_handler.setFormatter(bstack11111ll1lll_opy_)
  bstack11111l11ll1_opy_.setFormatter(bstack11111ll1lll_opy_)
  file_handler.setLevel(logging.DEBUG)
  bstack11111l11ll1_opy_.setLevel(log_level)
  file_handler.addFilter(lambda r: r.name != bstack1l1_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯࠱ࡻࡪࡨࡤࡳ࡫ࡹࡩࡷ࠴ࡲࡦ࡯ࡲࡸࡪ࠴ࡲࡦ࡯ࡲࡸࡪࡥࡣࡰࡰࡱࡩࡨࡺࡩࡰࡰࠪị"))
  logging.getLogger().setLevel(logging.DEBUG)
  bstack11111l11ll1_opy_.setLevel(bstack11111l11lll_opy_)
  logging.getLogger().addHandler(bstack11111l11ll1_opy_)
  logging.getLogger().addHandler(file_handler)
  return bstack11111l11lll_opy_
def bstack11111l1l111_opy_(config):
  try:
    bstack11111lll111_opy_ = set(bstack11l11l1llll_opy_)
    bstack11111l1lll1_opy_ = bstack1l1_opy_ (u"ࠩࠪỌ")
    with open(bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡱࡱ࠭ọ")) as bstack11111ll1l1l_opy_:
      bstack11111ll11l1_opy_ = bstack11111ll1l1l_opy_.read()
      bstack11111l1lll1_opy_ = re.sub(bstack1l1_opy_ (u"ࡶࠬࡤࠨ࡝ࡵ࠮࠭ࡄࠩ࠮ࠫࠦ࡟ࡲࠬỎ"), bstack1l1_opy_ (u"ࠬ࠭ỏ"), bstack11111ll11l1_opy_, flags=re.M)
      bstack11111l1lll1_opy_ = re.sub(
        bstack1l1_opy_ (u"ࡸࠧ࡟ࠪ࡟ࡷ࠰࠯࠿ࠩࠩỐ") + bstack1l1_opy_ (u"ࠧࡽࠩố").join(bstack11111lll111_opy_) + bstack1l1_opy_ (u"ࠨࠫ࠱࠮ࠩ࠭Ồ"),
        bstack1l1_opy_ (u"ࡴࠪࡠ࠷ࡀࠠ࡜ࡔࡈࡈࡆࡉࡔࡆࡆࡠࠫồ"),
        bstack11111l1lll1_opy_, flags=re.M | re.I
      )
    def bstack11111lll11l_opy_(dic):
      bstack11111l1ll11_opy_ = {}
      for key, value in dic.items():
        if key in bstack11111lll111_opy_:
          bstack11111l1ll11_opy_[key] = bstack1l1_opy_ (u"ࠪ࡟ࡗࡋࡄࡂࡅࡗࡉࡉࡣࠧỔ")
        else:
          if isinstance(value, dict):
            bstack11111l1ll11_opy_[key] = bstack11111lll11l_opy_(value)
          else:
            bstack11111l1ll11_opy_[key] = value
      return bstack11111l1ll11_opy_
    bstack11111l1ll11_opy_ = bstack11111lll11l_opy_(config)
    return {
      bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡽࡲࡲࠧổ"): bstack11111l1lll1_opy_,
      bstack1l1_opy_ (u"ࠬ࡬ࡩ࡯ࡣ࡯ࡧࡴࡴࡦࡪࡩ࠱࡮ࡸࡵ࡮ࠨỖ"): json.dumps(bstack11111l1ll11_opy_)
    }
  except Exception as e:
    return {}
def bstack11111ll1ll1_opy_(inipath, rootpath):
  log_dir = os.path.join(os.getcwd(), bstack1l1_opy_ (u"࠭࡬ࡰࡩࠪỗ"))
  if not os.path.exists(log_dir):
    os.makedirs(log_dir)
  bstack11111ll11ll_opy_ = os.path.join(log_dir, bstack1l1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࡟ࡤࡱࡱࡪ࡮࡭ࡳࠨỘ"))
  if not os.path.exists(bstack11111ll11ll_opy_):
    bstack11111l1l1l1_opy_ = {
      bstack1l1_opy_ (u"ࠣ࡫ࡱ࡭ࡵࡧࡴࡩࠤộ"): str(inipath),
      bstack1l1_opy_ (u"ࠤࡵࡳࡴࡺࡰࡢࡶ࡫ࠦỚ"): str(rootpath)
    }
    with open(os.path.join(log_dir, bstack1l1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡧࡴࡴࡦࡪࡩࡶ࠲࡯ࡹ࡯࡯ࠩớ")), bstack1l1_opy_ (u"ࠫࡼ࠭Ờ")) as bstack11111ll1111_opy_:
      bstack11111ll1111_opy_.write(json.dumps(bstack11111l1l1l1_opy_))
def bstack11111l1l11l_opy_():
  try:
    bstack11111ll11ll_opy_ = os.path.join(os.getcwd(), bstack1l1_opy_ (u"ࠬࡲ࡯ࡨࠩờ"), bstack1l1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡣࡰࡰࡩ࡭࡬ࡹ࠮࡫ࡵࡲࡲࠬỞ"))
    if os.path.exists(bstack11111ll11ll_opy_):
      with open(bstack11111ll11ll_opy_, bstack1l1_opy_ (u"ࠧࡳࠩở")) as bstack11111ll1111_opy_:
        bstack11111ll111l_opy_ = json.load(bstack11111ll1111_opy_)
      return bstack11111ll111l_opy_.get(bstack1l1_opy_ (u"ࠨ࡫ࡱ࡭ࡵࡧࡴࡩࠩỠ"), bstack1l1_opy_ (u"ࠩࠪỡ")), bstack11111ll111l_opy_.get(bstack1l1_opy_ (u"ࠪࡶࡴࡵࡴࡱࡣࡷ࡬ࠬỢ"), bstack1l1_opy_ (u"ࠫࠬợ"))
  except:
    pass
  return None, None
def bstack11111l11l1l_opy_():
  try:
    bstack11111ll11ll_opy_ = os.path.join(os.getcwd(), bstack1l1_opy_ (u"ࠬࡲ࡯ࡨࠩỤ"), bstack1l1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡣࡰࡰࡩ࡭࡬ࡹ࠮࡫ࡵࡲࡲࠬụ"))
    if os.path.exists(bstack11111ll11ll_opy_):
      os.remove(bstack11111ll11ll_opy_)
  except:
    pass
def bstack1l1lll1l_opy_(config):
  try:
    from bstack_utils.helper import bstack11l11111_opy_, bstack11ll11llll_opy_
    from browserstack_sdk.sdk_cli.cli import cli
    global bstack11111l1llll_opy_
    if config.get(bstack1l1_opy_ (u"ࠧࡥ࡫ࡶࡥࡧࡲࡥࡂࡷࡷࡳࡈࡧࡰࡵࡷࡵࡩࡑࡵࡧࡴࠩỦ"), False):
      return
    uuid = os.getenv(bstack1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ủ")) if os.getenv(bstack1l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧỨ")) else bstack11l11111_opy_.get_property(bstack1l1_opy_ (u"ࠥࡷࡩࡱࡒࡶࡰࡌࡨࠧứ"))
    if not uuid or uuid == bstack1l1_opy_ (u"ࠫࡳࡻ࡬࡭ࠩỪ"):
      return
    bstack11111l1ll1l_opy_ = [bstack1l1_opy_ (u"ࠬࡸࡥࡲࡷ࡬ࡶࡪࡳࡥ࡯ࡶࡶ࠲ࡹࡾࡴࠨừ"), bstack1l1_opy_ (u"࠭ࡐࡪࡲࡩ࡭ࡱ࡫ࠧỬ"), bstack1l1_opy_ (u"ࠧࡱࡻࡳࡶࡴࡰࡥࡤࡶ࠱ࡸࡴࡳ࡬ࠨử"), bstack11111l1llll_opy_, bstack11111l11l11_opy_]
    bstack11111ll1l11_opy_, root_path = bstack11111l1l11l_opy_()
    if bstack11111ll1l11_opy_ != None:
      bstack11111l1ll1l_opy_.append(bstack11111ll1l11_opy_)
    if root_path != None:
      bstack11111l1ll1l_opy_.append(os.path.join(root_path, bstack1l1_opy_ (u"ࠨࡥࡲࡲ࡫ࡺࡥࡴࡶ࠱ࡴࡾ࠭Ữ")))
    bstack1l1111l1ll_opy_()
    logging.shutdown()
    output_file = os.path.join(tempfile.gettempdir(), bstack1l1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠯࡯ࡳ࡬ࡹ࠭ࠨữ") + uuid + bstack1l1_opy_ (u"ࠪ࠲ࡹࡧࡲ࠯ࡩࡽࠫỰ"))
    with tarfile.open(output_file, bstack1l1_opy_ (u"ࠦࡼࡀࡧࡻࠤự")) as archive:
      for file in filter(lambda f: os.path.exists(f), bstack11111l1ll1l_opy_):
        try:
          archive.add(file,  arcname=os.path.basename(file))
        except:
          pass
      for name, data in bstack11111l1l111_opy_(config).items():
        tarinfo = tarfile.TarInfo(name)
        bstack11111lll1l1_opy_ = data.encode()
        tarinfo.size = len(bstack11111lll1l1_opy_)
        archive.addfile(tarinfo, io.BytesIO(bstack11111lll1l1_opy_))
    multipart_data = MultipartEncoder(
      fields= {
        bstack1l1_opy_ (u"ࠬࡪࡡࡵࡣࠪỲ"): (os.path.basename(output_file), open(os.path.abspath(output_file), bstack1l1_opy_ (u"࠭ࡲࡣࠩỳ")), bstack1l1_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡾ࠭ࡨࡼ࡬ࡴࠬỴ")),
        bstack1l1_opy_ (u"ࠨࡥ࡯࡭ࡪࡴࡴࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪỵ"): uuid
      }
    )
    bstack11111l111ll_opy_ = bstack11ll11llll_opy_(cli.config, [bstack1l1_opy_ (u"ࠤࡤࡴ࡮ࡹࠢỶ"), bstack1l1_opy_ (u"ࠥࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠥỷ"), bstack1l1_opy_ (u"ࠦࡺࡶ࡬ࡰࡣࡧࠦỸ")], bstack11l1l11111l_opy_)
    response = requests.post(
      bstack1l1_opy_ (u"ࠧࢁࡽ࠰ࡥ࡯࡭ࡪࡴࡴ࠮࡮ࡲ࡫ࡸ࠵ࡵࡱ࡮ࡲࡥࡩࠨỹ").format(bstack11111l111ll_opy_),
      data=multipart_data,
      headers={bstack1l1_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠬỺ"): multipart_data.content_type},
      auth=(config[bstack1l1_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩỻ")], config[bstack1l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫỼ")])
    )
    os.remove(output_file)
    if response.status_code != 200:
      get_logger().debug(bstack1l1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡࡷࡳࡰࡴࡧࡤࠡ࡮ࡲ࡫ࡸࡀࠠࠨỽ") + response.status_code)
  except Exception as e:
    get_logger().debug(bstack1l1_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡶࡩࡳࡪࡩ࡯ࡩࠣࡰࡴ࡭ࡳ࠻ࠩỾ") + str(e))
  finally:
    try:
      bstack1ll1l1l1l11_opy_()
      bstack11111l11l1l_opy_()
    except:
      pass